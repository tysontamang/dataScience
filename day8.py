#TASK1: create a dictionary with some values, then use for loop to access each and every elements

# #creating a dictionary
# dict={'fname':'ram',
#       'lname':'nepali',
#       'age':30}
# #using for loop to trigger those keys and values
# for i,j in dict.items():
#     # print(f'{i}: {j}',end='    ')
#     print('{1}:{1}'.format(i,j))

def sq(a):
    return a
list1=[1,2,3,4,5]
# sq(list1) #TypeError: unsupported operand type(s) for ** or pow(): 'list' and 'int'
# list2=list(map(sq,dict))
list2=list(map(sq,list1))
for i in list2:
    print(i)
