class Swimming:
    def swim():
        print("Swimming")
    
class Flying:
    def fly():
        print("Flying")

class Duck(Swimming,Flying):
    pass
obj = Duck()
Duck.swim()
Duck.fly()