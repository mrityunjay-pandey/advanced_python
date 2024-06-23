def number(num):
    num = num
    def adds():
        nonlocal num
        num += 5
        return num 
    return adds
num1 = number(5)
print(num1())
# jo bhi number user input karega usme 5 add ho jayega
# print(num1())