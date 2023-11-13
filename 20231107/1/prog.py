import collections

class DivStr(collections.UserString):
    def __init__(self, arg=""):
        super().__init__(arg)

    def __floordiv__(self, other):
        tmp = 0
        dist = len(self) // other
        for i in range(other):
            yield self[tmp:tmp + dist]
            tmp += dist

    def __mod__(self, other):
        return self[(len(self) // other) * other:]

'''a = DivStr("XcDfQWEasdERTdfgRTY")
print(* a // 4)
print(a % 4)
print(* a % 10 // 3)
print(a.lower() % 3)
print(* a[1:7] // 3)
print(a % 5 + DivStr() + a % 6)'''

import sys
exec(sys.stdin.read())