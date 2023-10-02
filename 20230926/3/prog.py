a = []
a.append(eval(input()))
n = len(a[0])
for i in range(n * 2 - 1):
    a.append(eval(input()))
ans = [[0] * n for i in range(n)]
for i in range(n):
    for j in range(n):
        for k in range(n):
            ans[i][j] += a[i][k] * a[n + k][j]

for i in ans:
    print(*i, sep = ', ')
