from abc import ABC, abstractmethod
class shape(ABC):
    @abstractmethod
    def area(self):
        pass

class circle(shape):
    pi=3.14
    def __init__(self, r):
        self.r=r
    def area(self):
        return self.pi*self.r**2

class rectangle(shape):
    def __init__(self,l,b):
        self.l=l
        self.b=b
    
    def area(self):
        return self.l*self.b

x=circle(3)
result=x.area()
print('area is ',result)

y=rectangle(4,5)
result=y.area()
print('area is ',result)
