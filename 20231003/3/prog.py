from math import *
def Calc(s, t, u):
    def res(x):
        f1 = lambda x : eval(s)
        f2 = lambda x : eval(t)
        f3 = lambda x, y : eval(u)
        return f3(f1(x), f2(x))
    return res

print(Calc(*eval(input()))(eval(input())))
