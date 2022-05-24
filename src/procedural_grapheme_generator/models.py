from dataclasses import dataclass, field


@dataclass
class board_base:
    size_x: int = 1
    size_y: int = 1
    matrix: list = []

    def reshape(self, size_x, size_y):
        pass


@dataclass
class board_default:
    size_x: int = 1
    size_y: int = 1
    matrix: list = []


@dataclass
class board(board_base, board_default):
    pass
