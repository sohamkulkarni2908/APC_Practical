def calculate_units(units):
    if units <= 100:
        return units * 5
    elif units <= 200:
        return 100 * 5 + (units - 100) * 7
    else:
        return 100 * 5 + 100 * 7 + (units - 200) * 10


def fixed_charge():
    return 100


def calculate_tax(amount):
    return amount * 0.05


def calculate_discount(amount):
    if amount > 2000:
        return amount * 0.10
    return 0


def final_bill(units):
    energy = calculate_units(units)
    fixed = fixed_charge()

    subtotal = energy + fixed
    tax = calculate_tax(subtotal)
    discount = calculate_discount(subtotal)

    return subtotal + tax - discount


units = int(input("Enter units consumed: "))
print("Final Electricity Bill:", final_bill(units))