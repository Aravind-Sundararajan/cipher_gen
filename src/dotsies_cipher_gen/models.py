from dataclasses import dataclass, field


class InvalidDimException(Exception):
    def __init__(self, n1, n2):
        self.message = f"{n1}!={n2}"


@dataclass(repr=True)
class plaintext_base:
    size: int = 4
    text: str = "test"

    def setText(self, t):
        self.size = len(t)
        self.text = t

    def getText(self) -> str:
        return self.text

    def getSize(self) -> int:
        return self.size


@dataclass(repr=True)
class plaintext_default:
    size: int = 4
    text: str = "test"


@dataclass(repr=True)
class plaintext(plaintext_base, plaintext_default):
    pass


@dataclass(repr=True)
class ciphertext_base:
    size_x: int = 6
    size_y: int = 1
    matrix: list[list[int]] = field(
        default_factory=lambda: [[0 for _ in range(5)]]
    )

    def setMatrix(self, m):
        self.matrix = m

    def reshape(self, sx, sy):
        a1 = self.size_x * self.size_y
        a2 = sx * sy
        if a1 == a2:
            pass  # FIXME
        else:
            raise InvalidDimException(a1, a2)

        self.size_x = sx
        self.size_y = sy


@dataclass(repr=True)
class ciphertext_default:
    size_x: int = 6
    size_y: int = 1
    matrix: list[list[int]] = field(
        default_factory=lambda: [[0 for _ in range(5)]]
    )


@dataclass(repr=True)
class ciphertext(ciphertext_base, ciphertext_default):
    pass
