from models import PlainText, CipherText
from multipledispatch import dispatch
import time
import timeit

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
        self._T = {}
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
        self._T[val] = key

    def get(self, key: str) -> list:
        return self.T[key]

    def find(self, key: tuple) -> str:
        return self._T[key]

class Parser:
    def __init__(self):
        self.T = Table()

    #@timer
    def convert(self, text):
        return self.ev(self.T, text)

    @dispatch(Table, CipherText)
    def ev(tab: Table, c: CipherText) -> PlainText:
        p = PlainText()
        t = [
            tab.find(c.state[b:b+c.shape[0]]) 
            for b in range(0,c.shape[0]*c.shape[1]-1,c.shape[0])
            ]
        p.setText("".join(t))
        return p

    @dispatch(Table, PlainText)
    def ev(tab: Table, p: PlainText) -> CipherText:
        c = CipherText(shape = (5,p.size))
        m = [a for letter in p.text for a in tab.get(letter)]
        c.setMatrix(tuple(m))
        return c

def test_p2c(p):
    parser = Parser()
    c = parser.convert(p)
    return c

def test_c2p(c):
    parser = Parser()
    p = parser.convert(c)
    return p

def test_circShift():
    p = PlainText(text=500000*"sphinx of the black quartz judge my vow!")
    parser = Parser()
    c = parser.convert(p)
    c.circShift(c.shape[0]*c.shape[1])
    new_p = parser.convert(c)
    c2 = parser.convert(new_p)
    assert p == new_p
    assert c == c2
    
p = PlainText(text=50000*"sphinx of the black quartz judge my vow!")
c = test_p2c(p)
p2 = test_c2p(c)
#print(timeit.timeit(stmt = lambda: test_p2c(p), number= 30)/30)
#print(timeit.timeit(stmt = lambda: test_c2p(c), number= 30)/30)