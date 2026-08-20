students = {
    "Nikhil": 85,
    "Siddhant": 72,
    "Nisarg": 88,
    "Chetan": 65
}

lowest = min(students, key=students.get)

print("Lowest marks:", students[lowest])
print("Student:", lowest)