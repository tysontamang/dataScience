# data1={"f_name":"ram",
#        "l_name":"lama",
#        "age":30}
# print(data1['f_name'])
# print(data1)
# print(data1.keys())
# print(data1.values())
#Q.WAP to
# glos={"":
#       "":
#       "":
#       "":
#       "":
# }

#creating a empty dict and inserting values later
dict={

}
# print(dict)
dict['one']=1 #inserting the value inside dict.
# print(dict)

#changing its value
dict["one"]=2
# print(dict)

#printing its keys and values

# print(dict.keys())
# print(dict.values())
# print(dict.items()) #returns the keys and values pair


#List inside a Dictionary

dict1={"club":"Barcelona",
    "country":"Spain",
    "player":['Araujo','marc','Cancelo']
}
#print(dict1['player']) #printing the values of player
dict1["player"][0]='hi' #updating list values inside a dict using indexing
#print(dict1['player'])

dict1['country']="Nepal" #updating values of a dict using keys
dict1['player'].append('hello') #appending a value to a list that is inside a dict
# print(dict1)

#Nesting with dictionary

dict3={'key1':{'key2':{'key3':'value'}
               }
               }
# print(dict3.keys())
# printa
(dict3.values())

dict3['key1']['key2']['key3']='newvalue' #changing values 
dict3['key3']='chaged' #changing values of nedted dict
# print(dict3)


#membership operator 'or'
'''
user_data=input('enter a character: ').lower()
if user_data=='a'or user_data=='e'or user_data=='i'or user_data=='o'or user_data=='u':
    print(user_data + ' is a vowel')
else:
    print(user_data + ' is not a vowel')
    print(user_data,"is not a vowel") '''

#leap year checking
'''
user_date=int(input('enter a year: '))
if user_date/4==0 and user_date/400==0 and user_date/100!=0:
    print(user_date , " is leap year.")
else:
    print(user_date , " is not a leap year") '''

#while loop
'''
n=5
while(n<=10):
    print("hi")
    n+=1
else:
    print("stop")
'''
'''
n=int(input('enter a number of a table you want: ' ))
m=1
while m<=10:
    print(n,"*",m ,'=', n*m,end='   ') #end sets next output to the end of the previous output eliminating the new line
    m+=1
else:
    print("Completed")
    '''

#print hello 7 times using while loop
'''
n=1
while n<=7:
    print("hi",n)
    n+=1
'''
'''
for i in range(5):
    for j in range(i):
        print('*',end='')
    print('*')
'''

