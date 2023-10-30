from itertools import tee, islice

def slide(seq, n):
    iters = tee(iter(seq))
    while True:
        yield from islice(iters[0], n)
        try:
            next(iters[1])
        except:
            break
        iters = tee(iters[1])

import sys
exec(sys.stdin.read())