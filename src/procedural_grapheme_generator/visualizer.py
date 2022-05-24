from models import Board
from matplotlib import pyplot as plt


class visualizer:
    def __init__(self):
        pass

    def show(self, board: Board):
        fig = plt.figure(figsize=(10, 10))
        ax = plt.axes()
        ax.set_axis_off()
        ax.imshow(board.matrix, interpolation="none", cmap="RdPu")
