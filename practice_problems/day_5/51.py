from abc import ABC,abstractmethod

class Employee(ABC):
    @abstractmethod
    def calculate_salary():
        pass

class PermanentEmployee(Employee):
    def __init__(self,base_salary, benefits):
        self.base_salary = base_salary
        self.benefits = benefits
    def calculate_salary(self):
        total_salary = self.base_salary + self.benefits
        print(f"Permanent Employee's total salary: {total_salary}")

class ContactEmployee(Employee):
    def __init__(self, hourly_rate, hours_worked):
        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked

    def calculate_salary(self):
        total_salary = self.hourly_rate * self.hours_worked
        print(f"Contract Employee's total salary: {total_salary}")


p1 = PermanentEmployee(50000,4000)
c1 = ContactEmployee(50,180)
p1.calculate_salary()
c1.calculate_salary()