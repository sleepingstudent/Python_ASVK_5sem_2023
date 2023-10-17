s = input().split()
d = dict()
for i in s:
    d.setdefault(i, 0)
print(*d.keys())
