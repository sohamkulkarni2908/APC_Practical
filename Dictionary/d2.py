employee = {
    "id": 101,
    "name": "Soham Kulkarni",
    "department": "IT",
    "salary": 50000
}

key = input("Enter key: ")

if key in employee:
    print("Value:", employee[key])
else:
    print("Key not found")