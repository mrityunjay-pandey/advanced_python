def sum (a,**b):
    sum = a
    for i in b:
        sum += i
    # print(a,b)
    return sum
print("Sum of any number of keyword arguments are: ",sum(5,10,56,6,8))