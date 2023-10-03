def Pareto(*a):
    res = []
    for i in range(len(a)):
        for j in range(len(a)):
            if a[i][0] <= a[j][0] and a[i][1] <= a[j][1] and (a[i][0] < a[j][0] or a[i][1] < a[j][1]):
                
                break
        else:
            res.append(a[i])
    return tuple(res)

a = eval(input())
b = Pareto(*a)
print(b)
