class LivingBeing:
    def live(self):
        print("Living")

class Animal(LivingBeing):
    def breathe(self):
        print("Breathing")

class Human(Animal):
    def speak(self):
        print("Speaking")

obj = Human()
obj.live()
obj.breathe()
obj.speak()