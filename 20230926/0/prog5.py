import pprint
ans = []

while (a := input()) and a:
    ans.append(eval(a))

ln = len(ans)
if all([len(el) == ln for el in ans]):
    for i in range(0, len(ans)):
        for j in range(0, i):
            ans[i][j], ans[j][i] = ans[j][i], ans[i][j]

for el in ans:
    print(*el)


