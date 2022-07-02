import os
import sys, os
from procedural_grapheme_generator.models import Board
from dotsies_cipher_gen.models import CipherText


class Board2CipherTextAdapter:
    def convert(self, b: Board) -> CipherText:
        c = CipherText(size_x = b.size_x, size_y = b.size_y, state=b.state)
        return c

class CipherText2BoardAdapter:
    def convert(self, b: CipherText) -> Board:
        c = Board(size_x = b.size_x, size_y = b.size_y, state=b.state)
        return c