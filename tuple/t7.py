employee_ids = (1001, 1002, 1003, 1004, 1005, 1006, 1007, 1008)
emp_id = int(input("Enter employee ID: "))

if emp_id in employee_ids:
    index = employee_ids.index(emp_id)
    print("Index of ID=", index)
else:
    print("ID not found")