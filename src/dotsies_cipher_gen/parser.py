from models import PlainText, CipherText
from multipledispatch import dispatch
import time

class Table:
    GLYPHS = "abcdefghijklmnopqrstuvwxyz !,.?'"
    DOTS = [
        tuple(int(x) for x in bin(i)[2:].rjust(5, "0"))
        for i in range(32)
    ]

    def __init__(self):
        self.T = {}
        self._T = {}
        for g, d in zip(self.GLYPHS, self.DOTS):
            self.T[g] = d
            self._T[d] = g

    def find(self, key: tuple) -> str:
        return self._T[key]

class Parser:
    def __init__(self):
        self.T = Table()

    def convert(self, text):
        return self.ev(self.T, text)

    @dispatch(Table, CipherText)
    def ev(tab: Table, c: CipherText) -> PlainText:
        t = [
            tab.find(c.state[b:b+c.shape[0]]) 
            for b in range(0,c.shape[0]*c.shape[1]-1,c.shape[0])
        ]
        return PlainText("".join(t))

    @dispatch(Table, PlainText)
    def ev(tab: Table, p: PlainText) -> CipherText:
        m = [a for letter in p.text for a in tab.T[letter]]
        return CipherText(shape=(5, p.size), data=tuple(m))

def test_p2c(p):
    parser = Parser()
    c = parser.convert(p)
    return c

def test_c2p(c):
    parser = Parser()
    p = parser.convert(c)
    return p

def test_circShift():
    p = PlainText(text=500000 * "sphinx of the black quartz judge my vow!")
    parser = Parser()
    c = parser.convert(p)
    c.circShift(c.shape[0] * c.shape[1])
    new_p = parser.convert(c)
    c2 = parser.convert(new_p)
    assert p == new_p
    assert c == c2
    
p = PlainText(text=50000 * "sphinx of the black quartz judge my vow!")
c = test_p2c(p)
p2 = test_c2p(c)
