class C:
    '''@property
    def field(self):
        return self._val
    
    @field.setter
    def field(self, value):
        self._val = value'''
    @property
    def age(self):
        if self._val == 42:
            print("secret value!")
            return -1
        return self._val
    
    @age.setter
    def age(self, value):
        if value <= 128:
            self._val = value
        else:
            print("Too old")
            raise ValueError
        
    