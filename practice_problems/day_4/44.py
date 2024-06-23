class ComplexNumber:
    def __init__(self,real,imaginary):
        self.real = real
        self.imaginary = imaginary

def add_complex_numbers(obj1,obj2):
    x = obj1.real + obj2.real
    y = obj1.imaginary + obj2.imaginary
    return ComplexNumber(x,y)
obj1 = ComplexNumber(2,3)
obj2 = ComplexNumber(1,2)
obj = add_complex_numbers(obj1,obj2)
print(f"After addition real part is {obj.real} and imaginary part is {obj.imaginary}")