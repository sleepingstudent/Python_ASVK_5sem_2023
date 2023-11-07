class A:
    def __str__(self):
        return A.__name__
class B(A):
    def __str__(self):
        return super().__str__() + ':' + B.__name__
    
class C(B):
    def __str__(self):
        return super().__str__() + ':' +  C.__name__
