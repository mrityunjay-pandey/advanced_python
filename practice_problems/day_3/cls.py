class Person:
    def __new__(self):
        print("This is a new method")
        self.__init__(self)
    def __init__(self):
        print("init method")

p = Person()