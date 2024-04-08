#TASK: print the odd number using lambda function

# list1=[1,2,3,4,5,6,7,8,9,10]
# result=list(filter(lambda a:a%2!=0,list1))
# # result=lambda a:a%2!=0,list1
# print(result) 

#user define function
# def area(a,b):
#     return a*b
# result1=area(3,4)
# print(result1)

# #user define class
# class area():
#     pass
#     def hi():
#         print('hi')
# result2=area()
# print(result2)

# class circle:
#     pi=3.14
# #circle get instantiated with a radius (default 1)
#     def __init__(self,radius=5):
#         self.leng=radius
#         self.area=self.pi*radius**2 #or we can write 
#     def setRadius(self,newRadius):
#         # print('you are inside setRadius')
#         self.radius1=newRadius
#         self.area1=self.pi*newRadius**2
#         self.circum=self.pi*2*newRadius
#     def circum2(self,radius3):
#         # print('you are inside circum2')
#         self.radius3=radius3
#         self.circum2=2*self.pi*radius3

# x=circle()
# print('radius=',x.leng)
# print('area=',x.area)

# y=circle()
# y.setRadius(6)
# print('radius=',y.radius1)
# print('area=',y.area1)
# print('circum=',y.circum)

# z=circle()
# z.circum2(7)
# print('radius=',z.radius3)
# print('circum=',z.circum2)

#attributes 

# class Dog:
#     def __init__(self,reed):       #method degine -->function
#         self.breed=d            #attribute



# class dog:
#     def breed():
#         print('the dog is german sheperd')
#     def eat():
#         print('the dog is eating')
#     def bark():
#         print('the dog is barking')
#     def sleep():
#         print('the dog is sleeping')
# x=dog()
# print(x.breed())


#Inheritance:
'''transter of charaacteristics from parent to derived/child class''' 

class rectangle():
    def __init__(self,l,b):
        self.l=l
        self.b=b
        self.area1=self.l*self.b
    def area(self,l,b):
        self.area1=self.l*self.b

class square(rectangle): #this is a child class
    def __init__(self,l,b):
        self.l=l
        self.b=b
    def sarea(self):
        self.sa=self.l*self.b

a=square(10,20)
a.sarea()
print(a.sa)



# class employee1():
#     def __init__(self,name,age,salary):
#         self.name=name
#         self.age=age
#         self.salary=salary
# class childemployee(employee1):
#     def __init__(self,name,age,salary,id):
#         self.name=name
#         self.age=age
#         self.salary=salary
#         self.id=id
# emp1=employee1('ram',2,1000)
# print(emp1.age)