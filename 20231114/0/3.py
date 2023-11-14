def repeat(n):
    def repaeter(fun):
        def newfun(*args, **kwargs):
            res = fun(*args, **kwargs)
            return [res for i in range(n)]
        return newfun
    return repaeter

@repeat(4)
def mult(a,b):
    return a*b

print(mult(8,9))