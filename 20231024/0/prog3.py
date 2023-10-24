from itertools import dropwhile, filterfalse, count

n = int(input())
ite = filterfalse(lambda x: x%n, count(1))
for i in range(100):
    print(next(ite))
