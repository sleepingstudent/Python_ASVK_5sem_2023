from decimal import *

def esum(N, one):
    tmp = 1
    ans = Decimal(0)
    print(type(one))
    #if idindtance(one, Decimal):
    for i in range(1, N):
        ans += one/type(one)(tmp)
        tmp *= i
    print(ans)

getcontext().prec = 40
esum(int(input()), eval(input()))
