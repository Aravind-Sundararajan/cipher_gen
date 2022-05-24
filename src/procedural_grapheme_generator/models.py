from dataclasses import dataclass, field
from enum import Enum
from operator import truediv


class _NONTOTALISTIC(Enum):
    "c"


@dataclass
class Rules_default:
    born: list = [3]
    survive: list = [2, 3]


@dataclass
class Rules_base:
    born: list = [3]
    survive: list = [2, 3]


@dataclass
class Rules(Rules_base, Rules_default):
    pass


@dataclass
class Board_base:
    size_x: int = 8
    size_y: int = 8
    matrix: list[list[int]] = field(
        default_factory=lambda: [[0 for i in range(8)] for j in range(8)]
    )

    def reshape(self, size_x, size_y):
        pass

    def eval(self):
        pass


@dataclass
class Board_default:
    size_x: int = 8
    size_y: int = 8
    matrix: list[list[int]] = field(
        default_factory=lambda: [[0 for i in range(8)] for j in range(8)]
    )


@dataclass
class Board(Board_base, Board_default):
    pass
