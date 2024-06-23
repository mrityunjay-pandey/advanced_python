num1 = int(input("Enter the number: "))
for i in range(2,(num1//2 + 1)):
    if (num1 % i == 0):
        print("Prime Number")
    else:
        print("Not a prime number")