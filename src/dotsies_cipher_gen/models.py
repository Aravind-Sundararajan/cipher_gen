import sys, os
sys.path.insert(0, os.path.abspath('./base'))
from dataclasses import dataclass, field
from base import Matrix, Matrix_base, Matrix_default
@dataclass(repr=True)
class PlainText_base:
    size: int = 4
    text: str = "test"

    def setText(self, t):
        self.size = len(t)
        self.text = t

    def getText(self) -> str:
        return self.text

    def getSize(self) -> int:
        return self.size


@dataclass(repr=True)
class PlainText_default:
    size: int = 4
    text: str = "test"


@dataclass(repr=True)
class PlainText(PlainText_base, PlainText_default):
    def __post_init__(self):
        self.size = len(self.text)

@dataclass(repr=True)
class CipherText_base(Matrix_base):
    shape: tuple[int] = (1,5)
    state: tuple[bool] = field(
        default_factory=tuple[bool]
    )
    def setMatrix(self, m):
        self.state = m

    def circShift(self,n: int):
        n = n % len(self.state)
        self.state = self.state[n:] + self.state[:n]

    def invert(self):
        self.state = [not elem for elem in self.state]

    def rotateRow(self, rid: int, dir: bool):
        ids = list(range(rid*self.shape[1], rid*self.shape[1] + self.shape[0]))
        temp = self.state[ids]
        direction =  2*int(dir)-1
        temp = temp[direction:] + temp[:direction]
        self.state[ids] = temp

    def rotateColumn(self, cid: int, dir: bool):
        ids = list(range(cid, self.shape[0]*self.shape[1], self.shape[0]))
        temp = self.state[ids]
        direction =  2*int(dir)-1
        temp = temp[direction:] + temp[:direction]
        self.state[ids] = temp

    def union(self, b):
        pass

    def intersection(self, b):
        pass

    def complement(self, b):
        pass

    def isValid(self) -> bool:
        pass


@dataclass(repr=True)
class CipherText_default(Matrix_default):
    shape: tuple[int] = (1,1)
    state: tuple[bool] = field(
        default_factory=tuple[bool]
    )


@dataclass(repr=True)
class CipherText(CipherText_base, CipherText_default):
    def __post_init__(self):
        self.state = tuple([bool(0)]*(self.shape[0]*self.shape[1]))
    def __repr__(self):
        return self.prettyPrint()
