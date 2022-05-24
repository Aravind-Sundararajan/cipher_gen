from models import plaintext, ciphertext
from multipledispatch import dispatch  # noqa


def letter2bitset(l: str) -> list:
    s = bin(ord(l))[3:]
    a = [0 for _ in range(6 - len(s))]
    a = a + [int(x) for x in s]
    return a


def bitset2letter(b: list) -> int:
    v = 32  # 64
    for x, i in enumerate(b[::-1]):
        v += i * 2 ** x
    return chr(v)


class Parser:
    def __init__(self):
        pass

    @dispatch(ciphertext)
    def eval(c: ciphertext) -> plaintext:
        p = plaintext()
        t = ""
        for b in c.matrix:
            t += bitset2letter(b)
        p.setText(t)
        return p

    @dispatch(plaintext)
    def eval(p: plaintext) -> ciphertext:
        c = ciphertext()
        m = [letter2bitset(letter) for letter in p.text]
        c.setMatrix(m)
        return c


p = plaintext(text="abcdefghijklmnopqrstuvwxyz;',.! ")
parser = Parser()
new_c = parser.eval(p)
new_p = parser.eval(new_c)
print(new_c)
print(new_p)
