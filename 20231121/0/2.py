import sys

print(sys.argv[1])
with open(sys.argv[1], 'r') as f:
    a = f.read()
    sze = len(a)
    #print(a[:sze // 3])
    id = a.find('\n', sze//3)
    print(a[:id])