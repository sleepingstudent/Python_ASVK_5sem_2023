s = input().split()
d = dict()
for i in s:
    #d.setdefaul(i, 0)
    d[i] = d.get(i, 0) + 1
print(d)
     
