# class Function:
#     var1 = 3
#     def keywords (self,age,salary):
#         self.age = age
#         self.salary = salary
#     def display(self):
#         print(self.age,self.salary)
    
# o1 = Function()
# o1.keywords(5,2333)
# o1.display()
# class Greeting:
#     message = "Hello, World!"
#     def say_hello(self):
#         print(self.message)

# greet = Greeting()
# greet.say_hello()
class Number:
    evens = []
    odds = []
    def __init__(self,num):
        self.num = num
        if num % 2 == 0:
            Number.evens.append(num)
        else:
            Number.odds.append(num)
N1 = Number(21)
N2 = Number(32)
N3 = Number(43)
N4 = Number(54)
N5 = Number(65)
print("even Numbers are:",Number.evens)
print("odd Numbers are:",Number.odds)
print("even Numbers are:",N1.evens)
print("odd Numbers are:",N1.odds)