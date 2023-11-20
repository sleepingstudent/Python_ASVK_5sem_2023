class Alpha:
    __slots__ = [i for i in 'abcdefghijklmnopqrstuvwxyz']

    def __init__(self, **kwargs):
        for i in kwargs:
            setattr(self, i, kwargs[i])

    def __str__(self, **kwargs):
        ans = ''
        for i in self.__slots__:
            val = getattr(self, i, None)
            if not (val is None):
                tmp = f"{i}: {val}, "
                ans += tmp
                
        if ans:
            return ans[:-2]
        else:
            return ans


class AlphaQ:
    def __init__(self, **kwargs):
        for i in kwargs:
            setattr(self, i, kwargs[i])

    def __setattr__(self, name, val):
        if name not in 'abcdefghijklmnopqrstuvwxyz' or len(name) != 1:
            raise AttributeError
        
        self.__dict__[name] = val

    def __getattr__(self, name):
        if name in self.__dict__:
            return self.__dict__[name]
        else:
            raise AttributeError

    def __str__(self):
        ans = ''
        for elem in 'abcdefghijklmnopqrstuvwxyz':
            value = getattr(self, elem)
            if value is not None:
                tmp = f"{elem}: {value}, "
                ans += tmp
        if ans:
            return ans[:-2]
        else:
            return ans


import sys
exec(sys.stdin.read())