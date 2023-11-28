class C:
    def __init__(self, a,b,c):
        self.a, self.b, self.c = a,b,c

a,b,c = input().split()
c = C(a,b,c)
print(c.a, c.b, c.c)
while s:=input():
    s = s.split()
    match s:
        case [c.a, *vars] if "yes" in vars:
            print("first")
        case [c.b]:
            print("second")
        case [c.c, *_, c.a]:
            print("3333")
        case _:
            print("Wat")