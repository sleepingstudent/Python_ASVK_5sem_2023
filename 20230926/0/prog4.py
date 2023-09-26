import pprint
ans = []

while (a := input()) and a:
    ans.append(eval(a))

for i in range(0, len(ans)):
    for j in range(0, i):
        ans[i][j], ans[j][i] = ans[j][i], ans[i][j]

#pprint.pprint(ans)

for el in ans:
    print(*el)


