class Shape:
    def area(self):
        return 0
    
class Circle(Shape):
    def __init__(self,r):
        self.r = r
    def area (self):
        return 3.14 * self.r * self.r
class Rectangle(Shape):
    def __init__(self,l,b):
        self.l = l
        self.b = b
    def area(self):
        return self.l * self.b
    
c1 = Circle(5)
r1 = Rectangle(5,4)
print(c1.area())
print(r1.area())