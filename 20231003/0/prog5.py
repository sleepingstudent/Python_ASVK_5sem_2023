def foo(a, b):
    return lambda x : a * x + b
#linear = lambda a, b : lambda x : a * x + b

f = foo(3, 4)
print(f(5))
