num1 = int(input("Enter 1st number : "))
num2 = int(input("Enter 2nd number : "))
num3 = int(input("Enter 3rd number : "))
##Method :- 1
# if ((num1 > num2) and (num1 > num3)):
#     print(num1,"is greatest")
# elif ((num2 > num1) and (num2 > num3)):
#     print(num2, "is greatest")
# else:
#     print(num3,"is greatest")


#Method :- 2 
if (num1 > num2):
    if (num1 > num3):
        print(num1,"is greatest")
    else:
        print(num3,"is greatest")
elif(num2 > num3):
    print(num2, "is greatest")