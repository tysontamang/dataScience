# TASK1: with the concept of class and object, calculate the perimenter of a circle 
class circle:
    pi=3.14
    def peri(self,r):
        self.r=r
        self.perimeter=2*self.pi*self.r

x=circle()  #creating object
x.peri(2)   #calling the function peri
result=x.perimeter #accessing the variable
print('the prerimeter is ',result)