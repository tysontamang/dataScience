#It is a property of an object which allows it to take multiple forms.
'''Many different routes you come acress for the same destination depending on the 
traffic, from a programming point of view this is called 'polymorphism' '''

# class bird:
#     def intro(self):
#         print('introduction')
#     def fly(self):
#         print('Flying')

# class pigeon(bird):
#     def fly(self):                      #method override by the child class pigeon within itself
#         print('pigeon is flying')

# class penguine(bird):
#     def fly(self):                      #method override by the child class penguine within itself
#         print('penguine can not fly')

# x=bird()
# x.intro()
# x.fly()

# y=pigeon()
# y.fly()
# y.intro()

# z=penguine()
# z.fly()
# z.intro()




#TASK2: with the concept of inheritance and polymorphish, prepare a class of lab with 
# their 2 attributes and implement this in another class, needed object and print the 
# values of their defined methods.

class lab:
    def __init__(self):
        print('lab is created')
    def door(self,n):   
        self.n=n 
        return self.n
class computer(lab):
    def __init__(self):
        print('computer lab is created' )
    def status(self,working):
        self.w=working
        print('working no of computer is ',self.w)

class chemistry(lab):
    def __init__(self):
        print('there are chemicals in this lab')
    def status(self,check):
        if check=='open':
            print('lab is open')
        else:
            print('lab is close')

# x=lab()
# y=computer()
z=chemistry()

# y.status(12)
z.status('open')
no_door=z.door(4)
print('No of door in this lab is ',no_door)


#TASK: Bike Rental System :
''' brand,stock,hourly,price,late fine, new bike append '''


