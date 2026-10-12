import pandas as pd

data = {"Laptop": 50000,"Mouse": 800,"Keyboard": 1500,"Monitor": 12000,"Printer": 9000
}

s = pd.Series(data)

print("All Products and Prices:")
print(s)

s = s * 1.10
print("\nPrices after 10% increase:")
print(s)

print("\nMost Expensive Product:")
print(s.idxmax(), s.max())

print("\nProducts costing more than 1000:")
print(s[s > 1000])
