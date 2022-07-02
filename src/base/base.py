import os
from dataclasses import dataclass, field
dirname = os.path.dirname

class InvalidDimException(Exception):
    def __init__(self, n1, n2):
        self.message = f"{n1}!={n2}"

class InvalidIndexException(Exception):
    def __init__(self, x, y,sx,sy):
        self.message = f"[{x},{y}] is not a valid index of state which has size ({sx},{sy})"

@dataclass(repr=True)
class Matrix_base:
    shape: tuple[int] = (1,5)
    state: list[bool] = field(
        default_factory=lambda: [bool(0) for _ in range(5)]
    )

    def __call__(self,pos):
        x,y = pos
        self.__setitem__(x,y, not self.__getitem__((x,y)))

    def prettyPrint(self) -> str:
        out = ""
        for i in range(self.shape[1]):
            for j in range(self.shape[0]):
                #print(self.__getitem__((j,i)))
                out += str(int(self.__getitem__((j,i))))
            out+= "\n"
        return out

    def __getitem__(self,pos) -> bool:
        x,y = pos
        return self.state[y*self.shape[0] + x]

    def __setitem__(self,pos,v: bool):
        x,y = pos
        self.state[y*self.shape[0] + x] = v

    def setState(self, m):
        self.state = m

    def reshape(self, sx, sy):
        a1 = self.shape[0] * self.shape[1]
        a2 = sx * sy
        if a1 == a2:
            pass  # FIXME
        else:
            raise InvalidDimException(a1, a2)

        self.shape[0] = sx
        self.shape[1] = sy

@dataclass
class Matrix_default:
    shape: tuple[int] = (1,1)
    state: list[bool] = field(
        default_factory=list[bool]
    )

@dataclass
class Matrix(Matrix_base, Matrix_default):
    pass

def py2ui(fpath):
    dirSRC = dirname(dirname(__file__))
    return os.path.join(dirSRC, "ui", os.path.split(fpath)[1][:-3] + ".ui")