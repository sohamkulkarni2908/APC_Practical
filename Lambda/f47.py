students = [("Nikhil", 85), ("Siddhant", 70),("Nisarg", 95),("Shubham", 80)]

result = sorted(students, key=lambda x: x[1])
print("Students sorted by marks:")

for student in result:
    print(student)