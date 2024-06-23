class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def display(self):
        print(f"name of the person is {self.name} and age is {self.age}")

p1 = Person("Anurag",18)
p2 = Person("Saurabh",18)
Person.display(p1)
Person.display(p2)
p1.display()