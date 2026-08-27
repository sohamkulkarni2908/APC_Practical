employees = [("Nikhil", 45000),("Siddhant", 60000),("Nisarg", 50000),("Shubham", 75000)]

result = sorted(employees, key=lambda x: x[1])
print("Employees sorted by salary:")

for employee in result:
    print(employee)