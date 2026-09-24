class Camera:
    def take_photo(self):
        print("Taking photo...")

class Phone:
    def make_call(self):
        print("Making phone call...")

class Smartphone(Camera, Phone):
    def display(self):
        print("Smartphone")

phone = Smartphone()
phone.display()
phone.take_photo()
phone.make_call()