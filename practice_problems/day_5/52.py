class Person:
    def greet(self):
        print("Hello")
class Student(Person):
    def greet(self):
        print("Hello! I am a student.")
class Teacher(Person):
    def greet(self):
        print("Hello! I am a teacher.")

s1 = Student()
t1 = Teacher()
s1.greet()
t1.greet()