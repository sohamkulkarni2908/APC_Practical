import pandas as pd

data = {
    "Employee_ID": [101, 102, 103, 104, 105],
    "Name": ["Soham", "Nisarg", "Nikhil", "Rehan", "Chetan"],
    "Department": ["CSE", "IT", "CSE", "ENTC", "IT"],
    "Salary": [45000, 60000, 75000, 50000, 80000],
    "Experience": [2, 5, 7, 3, 8]
}
df = pd.DataFrame(data)

print("Employees with salary greater than 50000:")
print(df[df["Salary"] > 50000])
print()
print("\nAverage salary:", df["Salary"].mean())
print()
print("\nHighest salary:", df["Salary"].max())
print()
print("\nEmployee with highest experience:")
print(df.loc[df["Experience"].idxmax()])