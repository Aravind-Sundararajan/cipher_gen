from dataclasses import dataclass, field
from operator import truediv


class InvalidDimException(Exception):
    def __init__(self, n1, n2):
        self.message = f"{n1}!={n2}"


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
    pass


@dataclass(repr=True)
class CipherText_base:
    size_x: int = 5
    size_y: int = 1
    matrix: list[list[bool]] = field(
        default_factory=lambda: [[bool(0) for _ in range(5)]]
    )

    def setMatrix(self, m):
        self.matrix = m

    def reshape(self, sx, sy):
        a1 = self.size_x * self.size_y
        a2 = sx * sy
        if a1 == a2:
            pass  # FIXME
        else:
            raise InvalidDimException(a1, a2)

        self.size_x = sx
        self.size_y = sy
    
    def circShift(self):
        pass

    def invert(self):
        pass

    def rotateRow(self, rid: int, dir: bool):
        pass

    def rotateColumn(self, rid: int, dir: bool):
        pass

    def union(self, b):
        pass

    def intersection(self, b):
        pass

    def complement(self, b):
        pass

    def isValid(self) -> bool:
        if len(self.matrix[0]) == 5:
            return True


@dataclass(repr=True)
class CipherText_default:
    size_x: int = 5
    size_y: int = 1
    matrix: list[list[int]] = field(
        default_factory=lambda: [[0 for _ in range(5)]]
    )


@dataclass(repr=True)
class CipherText(CipherText_base, CipherText_default):
    pass
