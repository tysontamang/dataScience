#data structure: series(1D) and dataframe (2D)
import pandas as pd
import numpy as np
# data=pd.Series([0.25,0.5,0.74,3.0],index=['a','b','c','d']) #manually giving the index as a,b,c,d to the 1D elements
# print(data)
#size of series
# print("size:",data.size)
# print(data['d'])
# data2=data[data>1] #assign all the data values that satisfies the stated condition
# print(data2)

#finding average of elements in series
x=pd.Series([1,2,3,4,5,6,7],index=['a','b','c','d','e','f','g'])
# print("mean is: ",x.mean())
#finding maximum values in series
# print("max value : ",x.max())
#finding minimum value
# print("min value :",x.min())
#sorting values
# print("values in sorted order/:\n",x.sort_values())

#displaying unique values
# print(x.unique())

#summaries of series statistics
# print(x.describe())

#calculate cumulative frequency of the given series
# print(x.cumsum())

#empty data frame
# print(x)

z=pd.DataFrame(x)
# print(z)
z.columns=['list1'] #renames the column name into list1
# z['list1']=20 #changes all values of list1 to 20
z['list2']=20 #creates new column list2 with values 20
z['list3']=z['list1']+z['list2']
z.pop('list2')
# print(z)

#using drop an axis
z1=z.drop('list1',axis=1) #delete colums
z1=z.drop(index=['a','b'],axis=0) #delete rows based on the given index
# print(z1)


#open a file
path=r'csvSample/data.csv'
path2=r'csvSample/data1.csv'
path3=r'csvSample/sales_data_sample.csv'
path4=r'csvSample/sales_data_sample1.csv'
b=pd.read_csv(path,encoding='unicode_escape') #reads CSV file 
# c=b.to_string() #print in string; use to_string() to print entire dataframe
# b=pd.DataFrame(a)
# print(b.describe())
# print(b)  #by default it prints first 5 and last 5 rows
# print(b.head()) #prints first five rows by default
# print(b.head(15)) #prints first 15 rows 
# print(b.tail()) #prints last five rows by default
# print(b.tail(15)) #prints last 15 rows 
# print(b.info())  #prints detail information
# print(pd.options.display.max_rows) #checking max number of rows to print
# pd.options.display.max_rows=100 #setting max number of rows to print to 100
# print(pd.options.display.max_rows) 


