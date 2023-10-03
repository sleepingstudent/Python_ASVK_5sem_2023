def foo(n = 10):
    return foo(n - 1) * 2 + n if n > 0 else 1
n = int(input())
print(foo(n))
