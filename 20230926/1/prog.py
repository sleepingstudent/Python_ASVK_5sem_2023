m, n = eval(input())
print(a := [i for i in range(m, n) if all([i % j != 0 for j in range(2, i)])])
