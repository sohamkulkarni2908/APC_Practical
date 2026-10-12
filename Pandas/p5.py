import pandas as pd

data = {
    "Order ID" : [101,102,103,104,105],
    "Customer" : ["Soham", "Rehan", "Nikhil", "Nisarg", "Chetan"],
    "Product_Name": ["Laptop", "Mouse", "Keyboard", "Monitor", "Printer"],
    "Quantity" : [2,4,4,3,2],
    "Price" : [50000,1000,2000,10000,25000],
    "Discount" : [5000,100,200,1000,2500] 
}

df = pd.DataFrame(data)
df["Final Amount"] = (df["Price"] * df["Quantity"]) - df["Discount"]

print("All orders:",df)
print()

print("Orders above 5000", df[df["Final Amount"] > 5000])
print()

print("Highest Value Order: ", df["Final Amount"].max())
print()

print("Average Order Value: ",df["Final Amount"].mean())