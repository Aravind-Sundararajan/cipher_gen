from models import PlainText, CipherText
from multipledispatch import dispatch
import time

def timer(func):
    def wrap_func(*args, **kwargs):
        t1 = time.time()
        result = func(*args, **kwargs)
        t2 = time.time()
        print(f'Function {func.__name__!r} executed in {(t2-t1):.10f}s')
        return result
    return wrap_func

class Table:
    def __init__(self):
        self.T = {}
        self.glyphs = "abcdefghijklmnopqrstuvwxyz !,.?'"
        self.dots = []
        for i in range(32):
            s = bin(i)[2:]
            a = [0 for _ in range(5 - len(s))]
            a = a + [int(x) for x in s]
            self.dots.append(tuple(a))
        for g,d in zip(self.glyphs,self.dots):
            self.put(g,d)
            #print(g + " : " + str(self.T.get(g)) + " : " + str(sum(x * (2**i) for i,x in enumerate(self.T.get(g)))))
        self.key_list = list(self.T.keys())
        self.val_list = list(self.T.values())

    def put(self, key,val):
        self.T[key] = val
    
    def get(self, key: str) -> list:
        return self.T[key]

    def find(self, key: list) -> str:
        i = self.val_list.index(tuple(key))
        return self.key_list[i]

def letter2bitset(l: str) -> list:
    s = bin(ord(l))[4:]
    a = [0 for _ in range(5 - len(s))]
    a = a + [int(x) for x in s]
    return tuple(a)


def bitset2letter(b: tuple) -> int:
    v = 32  # 64
    for x, i in enumerate(b[::-1]):
        v += i * 2 ** x
    return chr(v)


class Parser:
    def __init__(self):
        self.T = Table()
    
    @timer
    def convert(self, text):
        return self.ev(self.T, text)

    @dispatch(Table, CipherText)
    def ev(tab: Table, c: CipherText) -> PlainText:
        p = PlainText()
        t = ""
        for b in range(0,c.shape[0]*c.shape[1]-1,c.shape[0]):
            this_cipher = c.state[b:b+c.shape[0]]
            t += tab.find(this_cipher)
        p.setText(t)
        return p

    @dispatch(Table, PlainText)
    def ev(tab: Table, p: PlainText) -> CipherText:
        c = CipherText(shape = (5,p.size))
        m = []
        for L in p.text:
            m = m + list(tab.get(L))
        c.setMatrix(m)
        return c


@timer
def test_p2c():
    p = PlainText(text=300*"sphinx of the black quartz judge my vow!")
    parser = Parser()
    c = parser.convert(p)
    p2 = parser.convert(c)
    assert p == p2


@timer
def test_circShift():
    p = PlainText(text=100*"don't forget to drink your ovaltine!")
    print(p)
    parser = Parser()
    new_c = parser.convert(p)
    for i in range(len(new_c.state)):
        new_c.circShift(1)
    new_p = parser.convert(new_c)
    new_c = parser.convert(new_p)
    print(new_p)

print("test plaintext -> cipher -> plaintext")
test_p2c()
# print("test circleshift (circleshifting too many times)")
# test_circShift()