import numpy as np
# import os
# try:
    # fileName='newfile.txt'
    # a1=open(fileName,'w')
    # print('file open successfully!!!')
    # a1.writelines('hi this is new line') #writing inside the file
    # a1.close()
    # a2=open(fileName,'r')
    # for i in a2:
        # print(i)
    # os.remove(fileName)
# except FileNotFoundError:
    # print('File not found.')

# array1=np.array([1,2,3,4,5]) #NameError: name 'np' is not defined
# print(np.__version__)


#0-dimension array
# array0=np.array(9)
# print(array0.ndim)

#1-dimension array
#0 dim array element feed
# array1=np.array([1,2,3])
# print(array1.ndim)

#2-dimenstion array
#1 dim array element feed

# array2=np.array([[1,2,3],[1,2,3],[1,2,3]])
# print(array2.ndim)
# print(array2)
#3-dimenstion array
#2 dim array element feed

# array3=np.array([[[1,1,1],[2,2,2]],[[1,1,1],[2,2,2]]])
# print(array3.ndim)
# print(array3)


#4-dimenstion array
#3 dim array element feed

# array4=np.array([[[[1,1],[2,2]],[[1,1],[2,2]]],[[[1,1],[2,2]],[[1,1],[2,2]]],[[[1,1],[2,2]],[[1,1],[2,2]]]])
# print(array4.ndim)
# print(array4)
# print(array4)
#TASK: 1D,2D,3D,0D

#converting an array into other dimension array
# test1=np.array([1,2,3],ndmin=5)
# print(test1)
# print('no. of dimenstion is: ',test1.ndim)

#indexing in 1 dimension

# z=np.array([1,2,3,4,5,6,7])
# z[0]=z[1]+z[2]
# print(z[1]+z[2])
# print(z[0])
# print(z)

#indexing in 2 dimension
# z=np.array([[1,2,3,4,5,6,7],[8,9,10,11,12,13,14]])
# print(z[0,6])
# print(z)

#randomly generate 3D- print array([2,2,1])
z=np.array([[[1,2,3],[4,5,6],[7,8,9]],[[10,11,12],[13,14,15],[16,17,18]],[[19,20,21],[22,23,24],[25,26,27]]])
print(z[2,2,1])

