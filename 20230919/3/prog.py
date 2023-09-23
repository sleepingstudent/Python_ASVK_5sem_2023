def sm_f(tmp):
    res = tmp % 10
    tmp //= 10
    while tmp > 0:
        res += tmp % 10
        tmp //= 10
    return res

n = int(input())
i = n
while i < n + 3:
    j = n
    while j < n + 3:
        print(i, "*", j, "=", end = " ")
        if sm_f(i * j) == 6:
            print(":=)", end = " ")
        else:
            print(i * j, end = " ")
        j += 1
    print()
    i += 1

