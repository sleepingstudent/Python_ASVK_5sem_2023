from math import sin
def scale(a, b, A, B, x):
    X = (x - a) * (B - A) / (b - a) + A 
    return X


for i in range(-20, 20):
    x = scale(-20, 20, -5, 5, i)
    print(" " * int(scale(0, 2, 0, 20, sin(x) + 1)), "*")

