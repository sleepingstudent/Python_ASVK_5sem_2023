'''class A(Exception):
    pass

class B(A):
    pass

class C(B):
    pass
class D(C):
    pass

for E in (A, B, C):
    try:
        raise E
    except B:
        print("B")
    except C as Ex:
        print("C")
    #except B:
    #    print("B")
    except A:
        print("A")'''


while True:
    try:
        val = int(input())
    except Exception:
        print("bad data, need input")
        continue
    else:
        print("all good")
        break