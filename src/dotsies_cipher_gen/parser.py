from models import PlainText, CipherText
from multipledispatch import dispatch
import time

def timer(func):
    def wrap_func(*args, **kwargs):
        t1 = time.time()
        result = func(*args, **kwargs)
        t2 = time.time()
        print(f'Function {func.__name__!r} executed in {(t2-t1):.4f}s')
        return result
    return wrap_func

class Table:
    def __init__(self):
        self.T = {}
        self.glyphs = "abcdefghijklmnopqrstuvwxyz "
        for g in self.glyphs:
            self.put(g,letter2bitset(g))
        self.key_list = list(self.T.keys())
        self.val_list = list(self.T.values())

    def put(self, key,val):
        self.T[key] = val
    
    def get(self, key: str) -> list:
        return self.T[key]

    def find(self, key: list) -> str:
        i = self.val_list.index(key)
        return self.key_list[i]

def letter2bitset(l: str) -> list:
    s = bin(ord(l))[4:]
    a = [0 for _ in range(5 - len(s))]
    a = a + [int(x) for x in s]
    return a


def bitset2letter(b: list) -> int:
    v = 32  # 64
    for x, i in enumerate(b[::-1]):
        v += i * 2 ** x
    return chr(v)


class Parser:
    @timer
    def __init__(self):
        self.T = Table()

    @timer
    def convert(self, text):
        return self.ev(self.T, text)

    @dispatch(Table, CipherText)
    def ev(tab: Table, c: CipherText) -> PlainText:
        p = PlainText()
        t = ""
        for b in c.matrix:
            t += tab.find(b)
        p.setText(t)
        return p

    @dispatch(Table, PlainText)
    def ev(tab: Table, p: PlainText) -> CipherText:
        c = CipherText()
        m = [tab.get(L) for L in p.text]
        c.setMatrix(m)
        return c

p = PlainText(text="sphinx of the black quartz judge my vow ")
parser = Parser()
new_c = parser.convert(p)
new_p = parser.convert(new_c)
print(p)
print(new_c)
print(new_p)