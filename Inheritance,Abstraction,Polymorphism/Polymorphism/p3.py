class Vehicle:
    def start(self):
        print("Vehicle is starting")

class Car(Vehicle):
    def start(self):
        print("Car is starting")

class Bike(Vehicle):
    def start(self):
        print("Bike is starting")

class Bus(Vehicle):
    def start(self):
        print("Bus is starting")

vehicles = [Car(), Bike(), Bus()]
for vehicle in vehicles:
    vehicle.start()