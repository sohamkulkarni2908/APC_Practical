employees = {
    "Nikhil": 45000,
    "Nisarg": 60000,
    "Siddhant": 75000,
    "Chetan": 40000
}

highest = max(employees.values())
lowest = min(employees.values())
average = sum(employees.values()) / len(employees)

print("Highest salary:", highest)
print("Lowest salary:", lowest)
print("Average salary:", average)

print("Employees earning more than ₹50,000:")
for name, salary in employees.items():
    if salary > 50000:
        print(name, ":", salary)