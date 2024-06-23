class Rectangle:
    def __init__(self,length,width):
        self.length = length
        self.width = width
    def area(self):
        return self.length * self.width
    def perimeter(self):
        return 2 * (self.length + self.width)
    
r1 = Rectangle(50,45)
# r1.length = 55
# r1.width = 65
print(r1.area())
print(r1.perimeter())