from math import sin
def scale(a, b, A, B, x):
    X = (x - a) * (B - A) / (b - a) + A 
    return X

a, b = eval(input())
scr = [[' '] * 60 for i in range(20)]
for i in range(0, 60):
    x = scale(0, 60, a, b, i)
    y = int(scale(0, 2, 0, 20, sin(x) + 1))
    scr[y][i] = "*"

tmp = "\n".join(["".join(s) for s in scr])
print(tmp)

