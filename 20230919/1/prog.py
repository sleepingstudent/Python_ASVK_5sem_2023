a = int(input())
print("A", end = " ")

if a % 25 == 0 and a % 2 == 0:
    print("+", end = " ")
else:
    print("-", end = " ")
print("B", end = " ")
if a % 25 == 0 and a % 2 == 1:
    print("+", end = " ")
else:
    print("-", end = " ")
print("C", end = " ")
if a % 8 == 0:
    print("+")
else:
    print("-")

