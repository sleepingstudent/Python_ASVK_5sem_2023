from itertools import dropwhile

def foo():
    i = 1
    sm = 0
    while True:
        sm += 1/i**2
        i += 1
        yield sm

ite = foo()
ite2 = dropwhile(lambda x : x < 1.6, ite)
for i in range(10):
    print(next(ite2))
