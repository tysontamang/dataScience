def usingfilter(a):
    return a%2==0
mylist=[2,3,4,5,6,7,8,9]
filterdata=list(filter(usingfilter,mylist)) 
print(filterdata)


def usingmap(a):
    return a%2==0
mylist=[2,3,4,5,6,7,8,9]
filterdata1=list(map(usingmap,mylist)) 
print(filterdata1)