a, b = list(range(5, 16)), list("abcdefghijk")
a[4:8] = b[-5:]
print(*a)

a = a[-1:len(a) // 2 - 1:-2]
print(*a)
