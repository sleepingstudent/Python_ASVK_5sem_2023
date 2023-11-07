class A:
    def __init__(self, val):
        self.val = val
    def __add__(self, other):
        return self.__class__(self.val + other.val)

class B(A):
    def __str__(self):
        return f"{self.val}"
b = B(10)
a = B(12)
print(a + b)
