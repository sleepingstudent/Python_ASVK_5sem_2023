'''class C:
    __slots__ = ["one", "two"]
    atr = 100500'''
from pympler import asizeof

class R:
    def __init__(self, val):
        self.x = val

class S:
    __slots__ = ["x"]
    def __init__(self, val):
        self.x = val


rl = [R(i) for i in range(100500)]
sl = [S(i) for i in range(100500)]


