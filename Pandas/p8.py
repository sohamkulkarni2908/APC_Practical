
import pandas as pd

data = {
    "Soham": 45000,
    "Nisarg": 60000,
    "Nikhil": 35000,
    "Chetan": 75000,
    "Shubham": 52000
}

s = pd.Series(data)

print("Employee Salaries:")
print(s)

print("Highest Salary:", s.max())
print("Lowest Salary:", s.min())
print("Average Salary:", s.mean())

print("Employees earning more than 50000:")
print(s[s > 50000])
