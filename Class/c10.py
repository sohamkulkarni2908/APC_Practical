class Vehicle:
    def __init__(self, vehicle_no, model, rental_rate, availability):
        self.vehicle_no = vehicle_no
        self.model = model
        self.rental_rate = rental_rate
        self.availability = availability

    def rent(self):
        if self.availability:
            self.availability = False
            print("Vehicle rented successfully")
        else:
            print("Vehicle is not available")

    def return_vehicle(self):
        self.availability = True
        print("Vehicle returned successfully")

    def calculate_charges(self, days):
        return self.rental_rate * days


v = Vehicle("MH12AB1234", "Swift", 1000, True)
v.rent()
days = 3
print("Rental Charges:", v.calculate_charges(days))
v.return_vehicle()