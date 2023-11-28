class C:
    a = "A"

s = input().split()
match s:
    case [C.a, *vars] if "B" in vars:
        print("oks")
    case _:
        print("not oks")