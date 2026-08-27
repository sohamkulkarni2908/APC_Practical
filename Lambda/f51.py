products = [("Laptop", 50000, 1),("Mouse", 800, 2),("Keyboard", 1500, 2),("Headphones", 2000, 1)]

def total_value(product):
    return product[1] * product[2]

values = list(map(lambda x: (x[0], total_value(x)), products))

expensive = list(filter(lambda x: x[1] > 1000, values))

sorted_products = sorted(values,key=lambda x: x[1])

print("Total value of each product:")
for product in values:
    print(product)

print("\nProducts costing more than ₹1,000:")
for product in expensive:
    print(product)

print("\nProducts sorted according to total value:")
for product in sorted_products:
    print(product)