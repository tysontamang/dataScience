import pandas as pd #panda helps to clean,manage, manipulate and alalyse data
import numpy as np
# print(pd.__version__)
dataset={
    'cars':['Hyundai','Tesla','Mercedes','vokswagen','Benz','Tata'],
    'mydata':[2,3,4,5,6,7]
}
# a=np.load('x_y.npz')
# dataset2=np.copy(a)
# result=pd.DataFrame(dataset) #arrange data in rows and columns i.e. 2-Dimensional
# result=pd.DataFrame(dataset2)
# print(result)

# x=[1,2,3,4,5,6]
# result1=pd.Series(x)
# print(result1)
# print(result1[1])
# result2=[pd.Series(x,index=['a','b','c','d','e','f'])]
# print(result2)

#keys/value pair objects as a series
students={
    'f_name':['lionel','taisan','raman'],
    'l_name':['messi','tamang','gayak'],
    'age':[36,30,54],
    'address':['spain','ktm','boudha']
}
result3=pd.Series(students)
print(result3)
result4=pd.DataFrame(students)
# print(result4)