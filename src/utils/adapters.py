from procedural_grapheme_generator.models import Board
from dotsies_cipher_gen.models import CipherText


class Board2CipherTextAdapter:
    @staticmethod
    def convert(board: Board) -> CipherText:
        return CipherText(size_x=board.size_x, size_y=board.size_y, state=board.state)


class CipherText2BoardAdapter:
    @staticmethod
    def convert(cipher_text: CipherText) -> Board:
        return Board(size_x=cipher_text.size_x, size_y=cipher_text.size_y, state=cipher_text.state)
