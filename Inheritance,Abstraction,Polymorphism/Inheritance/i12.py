class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def display_product(self):
        print("Product Name:", self.name)
        print("Price:", self.price)


class ElectronicProduct(Product):
    def __init__(self, name, price, brand, warranty):
        super().__init__(name, price)
        self.brand = brand
        self.warranty = warranty

    def discounted_price(self, discount):
        return self.price - (self.price * discount / 100)

    def display(self):
        self.display_product()
        print("Brand:", self.brand)
        print("Warranty:", self.warranty, "years")


product = ElectronicProduct("Laptop", 80000, "Acer", 2)
product.display()
print("Discounted Price:", product.discounted_price(10))