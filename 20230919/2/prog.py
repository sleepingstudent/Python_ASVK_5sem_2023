sm = 0
while sm < 22:
    tmp = int(input())
    if tmp < 1:
        print(tmp)
        break
    sm += tmp
else:
    print(sm)
