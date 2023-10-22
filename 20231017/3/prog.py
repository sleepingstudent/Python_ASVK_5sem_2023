w = int(input())
cntr = dict()
while (s := input()):
    tmp = ""
    for i in s:
        if i.isalpha():
            tmp += i
        else:
            tmp += ' '
    tmp = tmp.lower().split()
    for i in tmp:
        if len(i) == w:
            cntr[i] = cntr.get(i, 0) + 1
cntr = {i:j for i, j in cntr.items() if j == max(cntr.values())}
cntr = sorted(cntr)
print(*cntr)
#cntr = dict(sorted(cntr.items(), key = lambda item: (item[1], item[0])))


