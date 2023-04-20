import os
import sys

from dataclasses import dataclass, field
from typing import List, Tuple

from base import Matrix_base, Matrix_default


class Rules:
    def __init__(self, born: List[int] = [3], survive: List[int] = [2, 3]):
        self.born = born
        self.survive = survive


@dataclass
class Board(Matrix_default):
    rules: Rules = field(default_factory=Rules)

    def __post_init__(self):
        self.state = tuple([False] * (self.shape[0] * self.shape[1]))

    def step(self) -> None:
        new_state = []
        for i in range(self.shape[0]):
            for j in range(self.shape[1]):
                index = self.index((i, j))
                count = 0
                for di in [-1, 0, 1]:
                    for dj in [-1, 0, 1]:
                        if di == dj == 0:
                            continue
                        ni, nj = i + di, j + dj
                        if 0 <= ni < self.shape[0] and 0 <= nj < self.shape[1]:
                            count += self.state[self.index((ni, nj))]
                if self.state[index]:
                    new_state.append(count in self.rules.survive)
                else:
                    new_state.append(count in self.rules.born)
        self.state = tuple(new_state)

    def index(self, ij: Tuple[int, int]) -> int:
        i, j = ij
        return i * self.shape[1] + j


if __name__ == '__main__':
    b = Board(shape=(8, 8))
    b[1, 2] = True
    print(b)
    print(b[0, 0])
