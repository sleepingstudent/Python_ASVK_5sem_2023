import sys
class Omnibus:
    d = dict()

    def __init__(self):
        self.__dict__['lst_atr'] = []

    def __getattr__(self, item):
        return self.__class__.d[item]

    def __setattr__(self, key, value):
        self.__class__.d[key] = 1 + self.__class__.d.get(key, 0)
        self.lst_atr.append(key)

    def __delattr__(self, item):
        if item in self.__class__.d.keys() and item in self.lst_atr:
            del self.item
            self.lst_atr.remove(item)
            self.__class__.d[item] -= 1
            

exec(sys.stdin.read())