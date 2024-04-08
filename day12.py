import numpy as np
#1
# arr=np.array([1,2,3,4])
# print(arr[2]+arr[3]) # ==> 7

#2
# arr=np.array([[1,2,3,4,5],[6,7,8,9,10]])
# print(arr[1,4]) # ==> 10

#3
# arr=np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
# print(arr[0,1,2]) #==> 6

#4
# arr=np.array([1,2,3,4,5,6,7])
# print(arr[::2]) # ==>[1,3,5,7]

#TASK1:

# arr=np.array([1,2,3,4,5,6,7,8,9,10,11,12])
# print(arr.ndim) #checking the dimension of the array

# arr=np.array([1,2,3,4,5,6,7,8,9,10,11,12])
# print(arr.ndim)
# # print(arr)
# arr1=arr.reshape(2,6) #reshaping array into 2 rows with 6 elements
# print(arr1[1,5]) 
# print(arr1.ndim)
# print(arr1.shape) # gives the order of the array eg. (2,6)
# arr2=np.concatenate((arr1[0],arr1[1])) #joining the two list into one
# print(arr2)


#joining two array -> concatenation
# arr1=np.array([1,2,3,4])
# arr2=np.array([5,6,7,8])
# # arr3=np.concatenate(arr1,arr2) #TypeError: only integer scalar arrays can be converted to a scalar index
# arr3=np.concatenate((arr1,arr2))
# print(arr3)

#splitting an array
# arr=np.array([1,2,3,4,5,6,7])
# arr1=np.array_split(arr,1) # array_split(arrayname,no. of array you want to create) ;it will adjust its elements self while placing
# print(arr1)

#sorting an array
#bydefault in ascending order
# arr=np.array([4,5,12,6,65,69,3,42,12,2,1])
# arr1=np.sort(arr) #sorting 1D array
# print(arr1)

# arr=np.array([[4,5,12,6,65,69,3,42,12,2,1],[1,2,3,5,3,2,5,7,2,1,4]])
# arr1=np.sort(arr)  #sorting 2D array
# print(arr1)
#sorting in descending
# arr=np.array([4,5,12,6,65,69,3,42,12,2,1])
# arr1=-np.sort(-arr) #sorting 1D array
# print(arr1)

# arr=np.array([[4,5,12,6,65,69,3,42,12,2,1],[1,2,3,5,3,2,5,7,2,1,4]])
# arr1=-np.sort(-arr) #sorting 2D array descending using negative
# arr1=np.flip(np.sort(arr)) #sorting 2D array descending using flip to ascending array
# arr1=np.sort(arr) [::-1] #sorting 2D array descending using reverse
# print(arr1)


#searching
# arr=np.array([[4,5,12,6,65,69,3,42,12,2,1],[1,2,3,5,3,2,5,7,2,1,4]])
# b=np.where(arr==4) #==>(array([0, 1]), array([ 0, 10])) --> value 4 is present in index 0 and 1 position array of the array, values in present in 0 index of 0th position array and 10 index of 1th position array 
# print(b)


#numpy array
# x=np.arange(5)
# y=x**2
# # print(x)
# # print(y)

# np.savez("x_y.npz",x_axis=x,y_axis=y)  #saves the file in the working location

# load_xy=np.load('x_y.npz') #loads the file from the working location
# print(load_xy.files) #['x_axis','y_axis']
# x=load_xy['x_axis'] #assigning the 'x_axis' values to x
# print(x)
# y=load_xy['y_axis'] #assigning the 'y_axis' values to y
# print(y)

array1=np.array([10,20,30,40])
array2=np.array([40,30,20,10])
# sum=np.add(array1,array2)
# # print(sum)
# subt=np.subtract(array1,array2)
# # print(subt)
# mul=np.multiply(array1,array2)
# # print(mul)
# div=np.divide(array1,array2)
# # print(div)
# power=np.power(array1,3)
# # print(power)
# mod=np.mod(array1,array2) #mod() and Remainder() both are same, we can do anyone
# rem=np.remainder(array1,array2)
# # print(mod)
# # print(rem)

# divmod=np.divmod(array1,array2)
# print(divmod) #gives both quotients and remainder

#rounding decimal
#trunc() and fix()
# array3=np.trunc([2.253,2.643]) #the fractional part of the signed number x is discarded.
# array4=np.fix([2.253,2.643]) #Round to nearest integer towards zero.
# print(array3,array4)

#sumation over an axis
array3=np.array([1,2,3,4])
# print(array1)
# print(array2)
# print(array3)
# result=np.sum([array1,array2,array3],axis=0) #axis=0 adds all the number vertically
# print(result)

# result=np.sum([array1,array2,array3],axis=1) #axis=1 adds  all the number horizontally
# print(result)

# result=np.sum([array1,array2,array3],axis=1)
# print(result)


#cumulative sum--> cumsum()
# result=np.cumsum(array1)
# print(result)

#matrix multiplication
a=np.array([[1,2,3],[1,2,3]])
b=np.array([[1,2,3,],[1,2,3],[1,2,3]])
result=np.matmul(a,b)
print(result)

