def consultation_charges():
    return 500


def laboratory_charges():
    return float(input("Enter laboratory charges: "))


def medicine_charges():
    return float(input("Enter medicine charges: "))


def room_charges():
    days = int(input("Enter number of room days: "))
    return days * 1000


def final_bill(category):
    consultation = consultation_charges()
    laboratory = laboratory_charges()
    medicine = medicine_charges()
    room = room_charges()

    total = consultation + laboratory + medicine + room

    if category == "senior":
        discount = total * 0.20
    elif category == "regular":
        discount = total * 0.10
    else:
        discount = 0

    return total - discount


category = input("Enter patient category (senior/regular/other): ")

bill = final_bill(category)
print("Final Hospital Bill:", bill)