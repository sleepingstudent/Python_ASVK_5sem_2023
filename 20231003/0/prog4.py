def add2(a, b):
    def fun(x):
        return a(x) + b(x)
    return fun
    #return lambda x : a(x) + b(x)

print(add2(bin, hex)(17))
