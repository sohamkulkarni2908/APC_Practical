import pandas as pd

data = {
    "Product ID" : [101,102,103,104,105],
    "Product_Name": ["NoteBook", "Pen", "Calculator", "Bookset", "Colors"],
    "Quantity" : [200,400,14,23,52],
    "Price" : [50,10,850,500,250],
}

df = pd.DataFrame(data)
df["Total_Sales"] = df["Price"] * df["Quantity"]

print("Products with sales greater than 10000: ")
print(df[df["Total_Sales"]>10000])
print()

print("Product with maximum sales: ")
print(df["Total_Sales"].max())
print()

print("Average Sales: ")
print(df["Total_Sales"].mean())