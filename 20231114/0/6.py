class Desc:
    def __get__(self, obj, cls):
        print("GET", repr(obj), cls)
        return obj._val
    def __set__(self, obj, val):
        print("SET", repr(obj), val)
        obj._val = val

class C:
    data = Desc()
    def __str__(self):
        return f"<{self}>"

c = C()