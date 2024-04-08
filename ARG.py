# def myFunction(*a):
    # return a*2
# test=myFunction(10,20,30,50)
# a=[10,20,30]
# test1=myFunction(a)
# print(test)
# print(test1)
# print(type(a))
# 
#*args and **kwargs combinatino
def myChoice(*args,**kwargs):
    if 'fruit' and 'juice' in kwargs:
        print(f"I like {' and '.join(kwargs)} and my fav fruit is {kwargs['juice']}")
        print(f"may i have {kwargs['fruit']} juice please?")
    else:
        pass #if we don't have to print anything 

myChoice('eggs','fish',fruit='grapes',juice='mango')