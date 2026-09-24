class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __eq__(self, other):
        return self.price == other.price

    def __gt__(self, other):
        return self.price > other.price

product1 = Product("Laptop", 60000)
product2 = Product("Mobile", 30000)

if product1 == product2:
    print("Both products have the same price")
else:
    print("Products have different prices")

if product1 > product2:
    print(product1.name, "is more expensive")