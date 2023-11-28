class Doubleton(type):
    _instance = [None, None]
    _cnt = 1
    def __call__(cls, *args, **kw):
        cls._cnt ^= 1
        if cls._instance[0] is None:
            cls._instance[0] = super().__call__(*args, **kw)
        elif cls._instance[1] is None:
            cls._instance[1] = super().__call__(*args, **kw)
        return cls._instance[cls._cnt]
    
class C(metaclass=Doubleton): pass
print(*(C() for i in range(7)), sep="\n")