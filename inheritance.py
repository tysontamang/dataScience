#Inheritance

# class Animal:
#     def __init__(self):
#         print('Animal class is created')
#     def WhoIs(self):
#         print('Animal')
#     def eat(self):
#         print('Animal who eats')
# class Dog(Animal):
#     def WhoIs(self):
#         print('type of Animal')
#     def speak(self):
#         print('dog is barking')

# a=Animal()
# print(a)
# a.WhoIs()
# a.eat()

# b=Dog()
# b.speak()
# b.eat() #accessing parent class method from the child class object


class grandparent:
    def __init__(self):
        print('grand parent created')
    def grand(self):
        print('1st generation')
class parent(grandparent):
    def __init__(self):
        print('parent created')
    def parent(self):
        print('2nd generation')
class child(parent):
    def __init__(self):
        print('child created')
    def child(self):
        print('3rd generation')

x=grandparent()
y=parent()
z=child()
z.grand()

