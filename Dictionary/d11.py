students = {
    "Nikhil": 85,
    "Siddhant": 92,
    "Nisarg": 88,
    "Chetan": 95
}

highest = max(students, key=students.get)

print("Highest marks:", students[highest])
print("Student:", highest)