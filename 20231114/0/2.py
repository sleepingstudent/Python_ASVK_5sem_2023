from functools import wraps


def debug(fun):
    @wraps(fun)
    def wrapper(*args):
        for i in args:
            if isinstance(type(i), int):
                raise TypeError
                return
        res = fun(*args)
        return res
    return wrapper


@debug
def mult(a, b):
    """this is mult"""
    return a * b

print(mult(2,3))
try:
    mult(1,'etrt')
except Exception as er:
    print("Exception!", er.__class__.__name__)