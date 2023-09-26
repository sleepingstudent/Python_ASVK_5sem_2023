a = list(eval(input()))
n = len(a)
for i in range(0, n - 1):
    for j in range(0, n - 1 - i):
        if (a[j] ** 2) % 100 > (a[j + 1] ** 2) % 100:
            a[j], a[j + 1] = a[j + 1], a[j]
print(a)
