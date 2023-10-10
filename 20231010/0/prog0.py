from decimal import Decimal
from fractions import Fraction

def multiplier(x, y, Type):
    return Type(x) * Type(y)
x, y, Type = input().split()
Type = eval(Type)
print(multiplier(x, y, Type))
