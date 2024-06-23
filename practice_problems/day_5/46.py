class Animal:
    def sound():
        print("Some sound")
class Dog(Animal):
    def sound():
        print("Bark")

obj = Dog()
Dog.sound()