employees = [("Nikhil", "IT", 45000),("Siddhant", "HR", 60000),("Nisarg", "IT", 75000),("Shubham", "Sales", 50000)]

high_salary = list(filter(lambda x: x[2] > 50000, employees))

increased_salary = list(
    map(lambda x: (x[0], x[1], x[2] * 1.10), employees))

sorted_employees = sorted(employees, key=lambda x: x[2])

print("Employees earning more than ₹50,000:")
for employee in high_salary:
    print(employee)

print("\nSalaries after 10% increase:")
for employee in increased_salary:
    print(employee)

print("\nEmployees sorted according to salary:")
for employee in sorted_employees:
    print(employee)