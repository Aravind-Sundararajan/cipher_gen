import sys, os
sys.path.insert(0, os.path.abspath('./base'))
from dataclasses import dataclass, field
from enum import Enum
from operator import truediv
import random

from base import Matrix_base, Matrix_default


@dataclass
class Rules_default:
    born: list[int] = field(default_factory=lambda:[3]) 
    survive: list[int] = field(default_factory=lambda:[2, 3]) 


@dataclass
class Rules_base:
    born: list[int] = field(default_factory=lambda:[3]) 
    survive: list[int] = field(default_factory=lambda:[2, 3]) 


@dataclass
class Rules(Rules_base, Rules_default):
    pass


@dataclass
class Board_base(Matrix_base):

    def step(self, rules: Rules):
        pass


@dataclass
class Board_default(Matrix_default):
    pass


@dataclass
class Board(Board_base, Board_default):
    def __post_init__(self):
        self.state = tuple([bool(0) for j in range(self.shape[0]*self.shape[1])])
    def __repr__(self):
        return self.prettyPrint()

# b = Board(shape = (8,8))
# b[1,2]=True
# print(b)
# print(b[0,0])
