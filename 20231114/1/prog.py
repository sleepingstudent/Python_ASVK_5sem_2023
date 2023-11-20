def objcount(cls):
    class New_cls(cls):
        counter = 0
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.__class__.counter += 1

        def __del__(self):
            try:
                super().__del__()
            except Exception:
                pass
            self.__class__.counter -= 1
    return New_cls

import sys
exec(sys.stdin.read())