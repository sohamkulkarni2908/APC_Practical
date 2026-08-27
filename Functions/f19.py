def calc_bill(unit):
    if unit <= 100:
        bill = unit * 5
    elif unit <= 200:
        bill = 100 * 5 + (unit - 100) * 7
    else:
        bill = 100 * 5 + 100 * 7 + (unit - 200) * 10
    return bill

unit = int(input("Enter units consumed: "))
print("Electricity bill:", calc_bill(unit))