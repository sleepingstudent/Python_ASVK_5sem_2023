from itertools import dropwhile, filterfalse, count, repeat

def repeater(seq, n):
    for elem in seq:
        yield from repeat(elem, n)

seq = eval(input())
n = int(input())
ite = repeater(seq, n)
print(list(ite))


