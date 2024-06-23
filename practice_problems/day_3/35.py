class Student:
    school_name = "NIET"
    def __init__(self,name,ID):
        self.name = name
        self.ID = ID
    @classmethod
    def change_name(cls,new_school_name):
        Student.school_name = new_school_name
    def display(self):
        print(f"Name is {self.name} id is {self.ID} and school name is {Student.school_name}")

s1 = Student("Mrityunjay Pandey",52123)
s1.display()
s1.change_name("IIT BOMBAY")
s1.display()
# x = 7
# print(x)
# x = 12
# print(x)
