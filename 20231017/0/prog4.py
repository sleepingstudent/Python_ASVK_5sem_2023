from collections import Counter
import timeit

def f_d(s):
    d = dict()
    for i in s:
        d.setdefault(i, 0)
        d[i] += 1
        #d[i] = d.get(i, 0) + 1
def f_counter(s):
    Counter(s)

s = input().split()
num, tim = timeit.Timer('f_d(s)', globals = globals()).autorange()
num2, tim2 = timeit.Timer('f_counter(s)', globals = globals()).autorange()
print(tim / num)
print(tim2 / num2)
