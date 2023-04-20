from dataclasses import dataclass, field
from typing import List, Tuple


@dataclass
class PlainText:
    size: int = 4
    text: str = "test"

    def __post_init__(self):
        self.size = len(self.text)

    def set_text(self, text: str):
        self.size = len(text)
        self.text = text

    def get_text(self) -> str:
        return self.text

    def get_size(self) -> int:
        return self.size


@dataclass
class CipherText:
    shape: Tuple[int, int] = (1, 1)
    state: Tuple[bool, ...] = field(default_factory=lambda: (False,))

    def __post_init__(self):
        self.state = tuple([False] * (self.shape[0] * self.shape[1]))

    def set_matrix(self, matrix: List[List[bool]]):
        self.state = tuple(sum(matrix, []))

    def circ_shift(self, n: int):
        n = n % len(self.state)
        self.state = self.state[n:] + self.state[:n]

    def invert(self):
        self.state = [not elem for elem in self.state]

    def rotate_row(self, row_id: int, direction: bool):
        row_start = row_id * self.shape[1]
        row_end = row_start + self.shape[1]
        temp = list(self.state[row_start:row_end])
        shift = 1 if direction else -1
        temp = temp[shift:] + temp[:shift]
        self.state = self.state[:row_start] + tuple(temp) + self.state[row_end:]

    def rotate_column(self, col_id: int, direction: bool):
        temp = []
        for i in range(self.shape[0]):
            temp.append(self.state[col_id + i * self.shape[1]])
        shift = 1 if direction else -1
        temp = temp[shift:] + temp[:shift]
        for i in range(self.shape[0]):
            self.state[col_id + i * self.shape[1]] = temp[i]

    def union(self, other):
        if self.shape != other.shape:
            raise ValueError("Matrices must have the same shape to be unioned")
        
        for i in range(self.shape[0]):
            for j in range(self.shape[1]):
                self.state[i * self.shape[1] + j] = self.state[i * self.shape[1] + j] | other.state[i * self.shape[1] + j]

    def intersection(self, other):
        if self.shape != other.shape:
            raise ValueError("Matrices must have the same shape to be intersected")
        
        for i in range(self.shape[0]):
            for j in range(self.shape[1]):
                self.state[i * self.shape[1] + j] = self.state[i * self.shape[1] + j] & other.state[i * self.shape[1] + j]

    def complement(self, other):
        pass

    def is_valid(self) -> bool:
        pass


@dataclass
class Rules:
    born: List[int] = field(default_factory=lambda: [3])
    survive: List[int] = field(default_factory=lambda: [2, 3])


@dataclass
class Board(Matrix):
    def step(self, rules: Rules):
        pass
