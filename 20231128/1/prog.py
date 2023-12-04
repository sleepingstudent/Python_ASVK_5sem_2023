import inspect  

class dump(type):
    def __new__(metacls, name, parents, lst, **tmp):
        def wrap(foo, name):
            def fun(self, *args, **kwargs):
                st = f'{name}: {tuple(args)}, {kwargs}'
                print(st)

                return foo(self, *args, **kwargs)
            return fun
        for j in lst:
            if inspect.isfunction(lst[j]):
                lst[j] = wrap(lst[j], j)
        return super().__new__(metacls, name, parents, lst)

import sys
exec(sys.stdin.read())