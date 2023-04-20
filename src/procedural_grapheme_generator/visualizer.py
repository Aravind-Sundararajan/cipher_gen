from models import Board

import matplotlib.pyplot as plt


class Visualizer:
    def __init__(self):
        pass

    def show(self, board: Board) -> None:
        fig, ax = plt.subplots(figsize=(10, 10))
        ax.set_axis_off()
        ax.imshow(board.matrix, interpolation="none", cmap="RdPu")
        plt.show()
