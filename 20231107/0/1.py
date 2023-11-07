class A:
    v = 1
class B(A):
    v = 2
    def __init__(self, val):
        self.v = val

b = B(3)
print(b.v)
del(b.v)
print(b.v)
del(B.v)
print(b.v)