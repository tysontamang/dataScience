#lambda expression
square1=lambda b:b**2 #lambda: anonym func where b is a parameter
result1=square1(7)
print(result1)


#passing list into lambda function
mylist=[1,2,3,4,5,6,7]
result2=list(map(lambda c:c**2,mylist))
print(result2)
