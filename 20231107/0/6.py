from math import inf

def div_ab(a, b):
    return a / b

tmp = ((10,2),(1,0),(9,3))
#tmp = eval(input())

for i, j in tmp:
    try:
        val = div_ab(i, j)
    except ZeroDivisionError:
        print(inf)
    else:
        print(val)
