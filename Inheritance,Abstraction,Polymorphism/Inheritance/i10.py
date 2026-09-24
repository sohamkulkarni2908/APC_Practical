class Vehicle:
    def __init__(self, brand):
        self.brand = brand

    def display_vehicle(self):
        print("Brand:", self.brand)

class Car(Vehicle):
    def __init__(self, brand, model):
        super().__init__(brand)
        self.model = model

    def display_car(self):
        self.display_vehicle()
        print("Car Model:", self.model)

class Bike(Vehicle):
    def __init__(self, brand, model):
        super().__init__(brand)
        self.model = model

    def display_bike(self):
        self.display_vehicle()
        print("Bike Model:", self.model)

class SportsCar(Car):
    def __init__(self, brand, model, speed):
        super().__init__(brand, model)
        self.speed = speed

    def display(self):
        self.display_car()
        print("Top Speed:", self.speed, "km/h")

class ElectricBike(Bike):
    def __init__(self, brand, model, battery):
        super().__init__(brand, model)
        self.battery = battery

    def display(self):
        self.display_bike()
        print("Battery:", self.battery, "kWh")


sports_car = SportsCar("BMW", "M4", 250)
electric_bike = ElectricBike("Ather", "450X", 3.7)
print("Sports Car:")
sports_car.display()
print()
print("Electric Bike:")
electric_bike.display()