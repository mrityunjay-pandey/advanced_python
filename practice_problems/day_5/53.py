from abc import ABC,abstractmethod
class Application(ABC):
    @abstractmethod
    def turn_on(self):
        print("turned on now")
class WashingMachine(Application):
    def turn_on(self):
        print("Washing machine is now on")
class Refrigerator(Application):
    def turn_on(self):
        print("Regrigerator is now on")

w1 = WashingMachine()
r1 = Refrigerator()
w1.turn_on()
r1.turn_on()
