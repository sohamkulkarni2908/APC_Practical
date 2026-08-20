employees = {
    101: "Nikhil",
    102: "Siddhant",
    103: "Nisarg",
    104: "Chetan"
}

emp_id = int(input("Enter employee ID: "))

if emp_id in employees:
    print("Employee exists")
    print("Name:", employees[emp_id])
else:
    print("Employee does not exist")