import numpy

# speed=[99,88,67,88,11,103,94,77,85,86]
# x=numpy.mean(speed)
# print(x)
# x=numpy.median(speed)
# print(x)

ages=[5,12,45,3,56,76,34,2,1,21,54,67,78,54,43]
x=numpy.percentile(ages,75)
print(x)

#data distribution

# x=numpy.random.uniform(0.0,5.0,250)
# print(x)

#CODE1: Line chart
import matplotlib.pyplot as plt
data1=[30,1,40,2,50,60,8,90]
age=[1,2,3,4,5,6,7]
plt.ylabel('data1')
plt.xlabel('age')
plt.plot(data1)
plt.show()