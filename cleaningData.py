import pandas as pd
import numpy as np

a=pd.read_csv('csvSample/data.csv')
print(a)

#dropna and fillna
# result=a.dropna() #delete rows that have empty cell
# result=a.dropna(inplace=True) #inplace use to remove epmty rows of a dataframe NOTE: now the dropna(inplace=True) will NOT return a new DataFrame
# result=a.fillna('0') 
# result1=pd.DataFrame(a)
# print(a.to_string())   #print all rows
# print(result1.info())

#fillna
# a.fillna(100,inplace=True)  #fill all empty cell with value 100
# print(a.to_string())

'''fillna into specific column'''
a['Calories'].fillna(50,inplace=True) #Filling value into Calories column only
# print(a.to_string())

a['Pulse'].fillna(round(a['Pulse'].mean()),inplace=True) #calculating mean value of column Pulse and placing into pulse column only.
# print(a.to_string())

# print(round(a['Pulse'].mean())) 

# a['Duration'].fillna(round(a['Duration'].mode())[0])
# print(round(a['Duration'].mode())[0])
# a.to_csv('csvSample/updated_data1.csv')

# b=pd.read_csv('csvSample/updated_data1.csv')
# print(b.info())


#converting values in date data type
#string to timestamp
a['Date'] = pd.to_datetime(a['Date'],format='mixed',errors='coerce')
# print(a.dtypes)
a.to_csv('csvSample/updated_data.csv')
# b=pd.read_csv('csvSample/updated_data.csv')
# print(b.dtypes)
# print(a.info()) #prints more info including Dtype
# print(a.dtypes) #prints only the data types of the columns

#changing column data type/format


#checking if there is NULL value
print(a.isnull())
