products = {}

def add_product(name, price, quantity):
    products[name] = [price, quantity]

def remove_product(name):
    if name in products:
        del products[name]

def calculate_subtotal():
    total = 0

    for price, quantity in products.values():
        total += price * quantity

    return total

def coupon_discount(subtotal):
    if subtotal >= 2000:
        return subtotal * 0.10
    return 0

def calculate_gst(amount):
    return amount * 0.18

def generate_invoice():
    subtotal = calculate_subtotal()
    discount = coupon_discount(subtotal)

    amount_after_discount = subtotal - discount
    gst = calculate_gst(amount_after_discount)

    final_amount = amount_after_discount + gst

    print("\n----- INVOICE -----")

    for name, data in products.items():
        price = data[0]
        quantity = data[1]

        print(name, ":", price, "x", quantity)

    print("Subtotal:", subtotal)
    print("Discount:", discount)
    print("GST:", gst)
    print("Final Amount:", final_amount)


add_product("Laptop", 50000, 1)
add_product("Mouse", 1000, 2)
add_product("Keyboard", 1500, 1)
generate_invoice()