# x=5
# y='hi'
# print(x+y)          #TypeError: unsupported operand type(s) for +: 'int' and 'str'
# try:
#     print(x+y)
# except TypeError:
#     print('error')

# def abc(a,g):
#     return(a/g)

# try:
#     x=abc(0,1)
#     print(x)
# except ZeroDivisionError:
#     print('we can not divide by zero')

#TASK: 
list1=['a','e','i','o','u']
try:
    print(list1[10])
except IndexError:
    print('outside of the index range')

def logic(s):
    if s<=5:
        return s
    else:
        pass
i=logic(6)
try:
    print('square is: ',i**2)
except:
    print('this error will not stop the system')
finally:
    print('all i ')


def login(u,p):
    if u=='admin' and p=='admin':
        print('login success')
    else:
        print('username/password incorrect')

        