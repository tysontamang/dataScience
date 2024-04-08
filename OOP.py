class Car:
    wheel=4
print(type(Car))            #<class '__main__.Car'>
x=Car()                     #creating object of Class Car
print(x.wheel)              #call by object
print(Car.wheel)            #call by Class itself
