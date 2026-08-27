students = [("Nikhil", 85),("Siddhant", 70),("Nisarg", 95),("Shubham", 65),("Rehan", 80)]

def average_marks(students):
    total = sum(map(lambda x: x[1], students))
    return total / len(students)

average = average_marks(students)

above_75 = list(filter(lambda x: x[1] > 75, students))

sorted_students = sorted(students, key=lambda x: x[1])

print("Average Marks:", average)

print("\nStudents scoring above 75:")
for student in above_75:
    print(student)

print("\nStudents sorted according to marks:")
for student in sorted_students:
    print(student)