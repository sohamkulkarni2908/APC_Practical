class MobilePhone:
    def __init__(self, brand, model, storage, price):
        self.brand = brand
        self.model = model
        self.storage = storage
        self.price = price

    def display(self):
        print("Brand:", self.brand)
        print("Model:", self.model)
        print("Storage:", self.storage)
        print("Price:", self.price)

    def discount_price(self, discount):
        return self.price - (self.price * discount / 100)


m = MobilePhone("Samsung", "Galaxy A55", "128 GB", 30000)
m.display()
discount = 10
print("Price after discount:", m.discount_price(discount))