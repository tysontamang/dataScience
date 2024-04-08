#file I/O
'''
1. file is a named location on disk to store related information.
2. it is used to permanently store data when computer is turned off.
we use files for future use of the data
'''

#file operation
'''
1.open syntax==> open(file_name, mode), mode=> read(r), write(w), append(a), text(t),binary(b), updating(+)
2.read write
3.close syntax ==> close()
'''

# file1=open('file1.txt','r+') #FileNotFoundError: [Errno 2] No such file or directory: 'file1.txt'
# file1=open('file.txt','w')
# print(file1.mode)
# file1.write('this is 1st write')
# file1.close()

# file2=open('file.txt','a+')
# file2.write('this is 2nd write')
# file2.write('this is 3rd wrtite')
# print(file2.mode)
import os,shutil
# newfile=open('hello.txt','w')
# newfile.close()
#file handling
'''

'''

path1=r'/home/kabita/Desktop/data science/test.py'
data1=open(path1,'r')
for i in data1:
    print(i)