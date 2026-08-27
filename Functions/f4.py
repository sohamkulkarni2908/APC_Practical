def simple_interest(p, r, t):
    s = (p * r * t) / 100
    return s

p = float(input("Enter principal amount: "))
r = float(input("Enter rate of interest: "))
t = float(input("Enter time: "))

print("Simple Interest:", simple_interest(p, r, t))