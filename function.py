#function is a block of code to perform the particular task
#function is defined using 'def' keyword.
#creating a function

# def printgarne(kura):
#     print('k kura ho bhane '+ kura)
# #calling a function
# printgarne('khas kura')

#with return
# def func1():
#     return 5
# c=func1()
# print(c)

#code1
# def sum(a,b):
#     return a+b

# user_data1=int(input("enter first number: "))
# user_data2=int(input("enter second number: "))
# result=sum(user_data1,user_data2) #user_data1 and user_data2 are the values passing to the function
# print('the sum is : ',result)

# #code2
# def sub(a,b):
#     return a-b

# result2=sub(user_data1,user_data2) #user_data1 and user_data2 are the values passing to the function
# print('the difference is : ',result2)

# #code3
# def mul(a,b,c):
#     return a*b*c
# z=int(input('third number: '))
# q= mul(user_data1,user_data2,z)
# print('the multiplication is: ',q)

#TASK2: WAP using function to return the square of a number.
# def sq(a):
#     return a**2
# x=int(input("enter a number"))
# y=sq(x)
# print("the square is: ", y)

#function with list
def check(a):
    return a*2

list1=[2,3,4,5,6,7]
dict2={'one':1,'two':2}
# #a=dict2.values()
# a=check(list1)
# print(a)

# for i in list1:
#     result=check(i)
#     print(result,end=', ')

#MAP 
result=list(map(check,list1))
print(result)

# #result2=list(map(check,a))
# print(result2)

#TASK3: pass a list into a function and return the double
def double(a):
    return a*2
list2=[1,2,3,4,5,6,7,8,9]
result=list(map(double,list2))
print(result)
