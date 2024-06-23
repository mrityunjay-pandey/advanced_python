from functools import reduce
list1 = [1,2,3,4,5,6,7]
x = reduce(lambda x,y: x*y,list1)
print(x)