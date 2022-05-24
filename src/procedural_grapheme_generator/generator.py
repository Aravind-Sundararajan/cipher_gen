from models import Board, Rules
import random


class generator:
    def __init__(self):
        pass

    def simulate(self, board: Board, rules: Rules, iterations) -> Board:
        for i in range(iterations):
            board.step(rules)
        return board

    def setSeed(self, s: int):
        random.seed(s)
