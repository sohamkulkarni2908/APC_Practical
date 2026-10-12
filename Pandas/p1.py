import pandas as pd

data = {
    "Student_ID": [1, 2, 3, 4, 5],
    "Name": ["Nisarg", "Rehan", "Soham", "Nikhil", "chetan"],
    "Python": [80, 75, 90, 65, 85],
    "DBMS": [70, 80, 85, 60, 90],
    "Maths": [85, 70, 88, 75, 80]
}

df = pd.DataFrame(data)
print(df)

df["Total"] = df["Python"] + df["DBMS"] + df["Maths"]
df["Average"] = df["Total"] / 3

print("\nTotal and Average:")
print(df[["Name", "Total", "Average"]])

print("\nStudents with average above 75:")
print(df[df["Average"] > 75])