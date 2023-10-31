class Rectangle:
    rectcnt = 0 #we can use list rectcnt = [0]
    FMT = "{0}: ({1},{2})({1},{4})({3},{4})({2},{4})"
    def __init__(self, x1,y1,x2,y2):
        self.__class__.rectcnt += 1
        self.x1 = x1
        self.x2=x2
        self.y1=y1
        self.y2=y2
        self.data = [(x1,y1), (x1,y2), (x2,y2), (x2,y1)]
        setattr(self,'rect_' + str(self.rectcnt), self.rectcnt)
    def __str__(self):
        x1 = self.x1
        x2 = self.x2
        y1 = self.y1
        y2 = self.y2
        #st = str((x1,y1)) + str((x1,y2)) + str((x2,y2)) + str((x2,y1))
        return self.FMT.format(self.rectcnt, x1,y1,x2,y2)
    def square(self):
        return abs((self.x1 - self.x2) * (self.y1 - self.y2))
    def __lt__(self, obj):
        return self.square() < obj.square()
    def __eq__(self, obj):
        return self.square() == obj.square()
    def __mul__(self, a):
        return Rectangle(self.x1 * a, self.y1 * a, self.x2 * a, self.y2  * a)
    #__rmul__ = __mul__
    def __rmul__(self, a):
        return Rectangle(self.x1 * a, self.y1 * a, self.x2 * a, self.y2  * a)
    def __getitem__(self, i):
        return self.data[i]
    def __bool__(self):
        return self.square != 0
    def __del__(self):
        print('Deleting', self)
        self.__class__.rectcnt -= 1  
        
'''
r = Rectangle(0,0, 2,2)
r = Rectangle(0,0, 2,2)
r = Rectangle(0,0, 2,2)
r = Rectangle(0,0, 2,2)
print(r)
print(Rectangle.rectcnt)'''
