from math import *
def scale(a, b, A, B, x):
    X = (x - a) * (B - A) / (b - a) + A 
    return X

w, h, a, b, fnct = input().split()
w, h, a, b = int(w), int(h), int(a), int(b)
#a, b = eval(input())
scr = [[' '] * (w) for i in range(h)]
#fnct = eval(fnct)
x = a
mx_val, mn_val = round(eval(fnct)), round(eval(fnct))
for i in range(0, w):
    x = scale(0, w - 1, a, b, i)
    mx_val = max(mx_val, eval(fnct))
    mn_val = min(mn_val, eval(fnct))
for i in range(0, w):
    x = scale(0, w - 1, a, b, i)
    y = round(scale(mn_val, mx_val, 0, h - 1, eval(fnct)))
    scr[y][i] = "*"
    if i >= 1:
        fl = 1
        if y_lst > y:
            fl = -1
        for j in range(y_lst + 1, y):
            scr[j][i - 1 + (((y - y_lst) // 2) > j)] = '*'

        for j in range(y + 1, y_lst):
            scr[j][i - (((y - y_lst) // 2) > j)] = '*'
    y_lst = y
tmp = "\n".join(["".join(s) for s in scr[::-1]])
print(tmp)

