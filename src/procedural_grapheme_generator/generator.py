from models import Board, Rules
import random


class Generator:
    @staticmethod
    def simulate(board: Board, rules: Rules, iterations: int) -> Board:
        for _ in range(iterations):
            board.step(rules)
        return board

    @staticmethod
    def set_seed(seed: int) -> None:
        random.seed(seed)
