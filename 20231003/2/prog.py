def foo(val1, val2):
    if type(val1) in (tuple, list):
        res = []
        for i in val1:
            if i not in val2:
                res.append(i)
        return res
    else:
        return val1 - val2
a, b = eval(input())
print(type(a)(foo(a, b)))
