from abc import ABC , abstractmethod

class Shape(ABC):
    @abstractmethod
    def perimeter(self):
        pass
class Square(Shape):
    def __init__(self,a):
        self.a = a
    def perimeter(self):
        return 4 * self.a
    
class Triangle(Shape):
    def __init__(self,a,b,c):
        self.a = a
        self.b = b
        self.c = c
    def perimeter(self):
        return self.a + self.b + self.c
obj1 = Triangle(3,4,5)
obj2 = Square(4)
print(obj1.perimeter())
print(obj2.perimeter())
