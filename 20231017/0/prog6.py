st = input()
a, b = eval(input())
print(eval(st, {'x' : a, 'y' : b}))
print(eval(st, {'y' : a, 'x' : b}))
