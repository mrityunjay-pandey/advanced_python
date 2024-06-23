class MathOperations:
    # def __init__(self,a,b):
    #     self.a = a
    #     self.b = b
    @staticmethod
    def add(a,b):
        return a + b
    @staticmethod
    def sub(a,b):
        return a - b
    @staticmethod
    def mul(a,b):
        return a * b
    @staticmethod
    def div(a,b):
        return a/b
obj = MathOperations()
add = MathOperations.add(10,5)
sub = obj.sub(10,5)
mul = MathOperations.mul(10,5)
div = obj.div(10,5)

print(f"Addition: {add}")
print(f"Subtraction: {sub}")
print(f"Multiplication: {mul}")
print(f"Division: {div}")
    
