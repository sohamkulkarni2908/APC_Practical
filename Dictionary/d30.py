students = {
    "Nikhil": "CSE",
    "Nisarg": "IT",
    "Shubham": "CSE",
    "Sneha": "ENTC",
    "Rehan": "IT"
}

groups = {}

for name, department in students.items():
    if department not in groups:
        groups[department] = []

    groups[department].append(name)

print(groups)