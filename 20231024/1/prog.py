def fib(m, n):
    now, last = 1, 1
    for i in range(2, m + 1):
        last, now = now, last + now
    for i in range(m, m + n):
        yield now
        if i == 0:
            continue
        last, now = now, last + now

import sys
exec(sys.stdin.read())
