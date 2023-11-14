def check(type_name):
    def checker(fun):
        def newfun(*args):
            if all([isinstance(i, type_name) for i in args]):
                print("TYPE!")
                return fun(*args)
            else:
                print("another Type!")
                raise TypeError
        return newfun
    return checker



@check(int)
def mult(a,b):
    return a*b

print(mult(3,4))
print(mult(1231, [['dwdw']]))