# print(int(0b00011101))
# x = 29
# # print(bin(x))
# y = x>>4
# print(bin(y))
# print(y)
# x = 5 - 1
# y = 4
# print(x == y)
# print(x is y)
# print(5-1 == 4)
# print(5-1 is 4)
class Employee:
    company_name = "Google"
    def __init__(self,name,ID):
        self.name = name
        self.ID = ID
    def display(self):
        print(f"The name of the employee is {self.name} , id is {self.ID} and works in {Employee.company_name}")
e1 = Employee("Mrityunjay",231064)
e1.display()