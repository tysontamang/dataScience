
# list1=['ktm','pokhara','illam','jhapa']
# for i in list1:
#     print(i,end=', ')

#Iterating over dictionary
person = {'name':"Ram Bahadur", 'age':30,'city':'Ktm'}

# for i,j in person: #ValueError: too many values to unpack (expected 2)
#     print(i) 
# for key,value in person.items():
    # print(f"{key}:{value}",end=' ') #formatting the printed output
    # print(key)
    # print(value)
    # print(key,value)

#TASK: create a empty dictionary, feed the elements from outside, use for loop to access those filled elements

# task={}
# task['fname']='ram'
# task['lname']='nepali'
# task['age']=30
# for i,j in task.items():
#     print(f'{i}:{j}',end=' ')

#formatting
a='hey'
b='hare'
c=a+b+' {} ani {}'
print(c) #adding two string together
d='oh my god or {} and {}' 
print(d.format(a,b))  
print(c.format(a,b))
print(c)