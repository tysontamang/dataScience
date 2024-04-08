#'copy' and 'view'
#CODE1
import numpy as np
# array1=np.array([1,2,3,4,5,6,7])
# array2=np.copy(array1) #copy all array1 conntents into array2
# print(array2)
# array2[0]=9 #changing array2[0] value which do not changes the value to the original array1 
# print(array1)
# print(array2)


#CODE2
# array1=np.array([1,2,3,4,5,6,7])
# array2=array1.view()
# print(array2)
# array1[6]=200 #changing value in array1 which changes value in view array
# array2[0]=100 #changing value of array2 which changes value in original array1
# print(array2)
# print(array1)

#universal function
# x=1
# y=2
x=np.array([1,2,3,4,5])
y=np.array([6,7,8,9,10])
# test1=np.add(x,y) #add function
# print(test1) #here, we get output in the form of array, no comma used here
# print(type(test1)) #<class 'numpy.ndarray'>

#statistics
#abs,sin,sqrt,log,log10,exp,cos,tan...
# a=np.array([[1,2,3],[4,5,6]])
# print(np.abs(a))
# print(np.sinh(a))
# print(np.dot(x,y)) #gives dot product
# print(np.inner(x,y)) #inner gives dot product or scalar product
# a=np.array([1,2])
# b=np.array([6,7])
# c=np.array([[1,2],[3,4]])
# # print(np.outer(a,b)) #outer give vector product
# vals,vecs=np.linalg.eig(c)
# print(vals,vecs)

#inverse
a=np.array([[1,2],
            [4,5]])
b=np.linalg.inv(a) #to find inverse
print(b)