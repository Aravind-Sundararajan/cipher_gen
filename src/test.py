
import time

self.sz =1000

def timer(func):
    def wrap_func(*args, **kwargs):
        t1 = time.time()
        result = func(*args, **kwargs)
        t2 = time.time()
        print(f'Function {func.__name__!r} executed in {(t2-t1):.4f}s')
        return result
    return wrap_func
class ListTester:
    def __init__(self) -> None:
        self.sz = 1000

    @timer
    def createListComp(self) -> list:
        t = [[i for i in range(self.sz)] for j in range(self.sz)]
        return t

    @timer
    def create2DList(self) -> list:
        t = []
        for i in range(self.sz):
            for j in range(self.sz):
                t.append(j)
        return t

    @timer
    def scan2DList(self,t):
        for i in range(self.sz):
            for j in range(self.sz):
                t[i*self.sz + j]
    @timer
    def scanListOfList(self, t):
        self.sz = 1000
        for i in range(self.sz):
            for j in range(self.sz):
                t[i][j]

    @timer
    def scan2DList(self, t):
        self.sz = 1000
        for i in range(self.sz):
            for j in range(self.sz):
                t[i*self.sz + j]       

t1 = createListComp()
t2 = create2DList()
scanListOfList(t1)
scan2DList(t2)