class Vehicle:
    def drive():
        print("Driving")

class Car(Vehicle):
    def carry_passengers():
        print("carries passengers")
class Truck(Vehicle):
    def carry_cargo():
        print("carries cargo")
class PickupTruck(Car,Truck):
    pass

obj = PickupTruck
obj.drive()
obj.carry_passengers()
obj.carry_cargo()