import inspect

class A:
    val:int
    def __init__(self, val : int) -> None:
        a = inspect.get_annotations(self.__class__)
        if not isinstance(val, a['val']):
            raise TypeError("Must be int")
        self.val = val




'''def fun(a: int, b:str) -> str:
    return a*b
fun(3,"ER")
fun(3,4)
A = inspect.get_annotations(fun)
A['a'](123213)'''