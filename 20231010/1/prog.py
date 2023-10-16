from fractions import Fraction

st = input().split(',')
s, w = Fraction(st[0]), Fraction(st[1])
n1 = int(st[2])
A = Fraction(0)
B = Fraction(0)
for i in range(n1 + 1):
    A += Fraction(st[3 + i]) * s ** (n1 - i)
start = 3 + n1 + 1
n2 = int(st[start])
start += 1
for i in range(n2 + 1):
    B += Fraction(st[start + i]) * s ** (n2 - i)
if A / B == w:
    print("True")
else:
    print("False")
