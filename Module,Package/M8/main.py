from student.marks import total, percentage
from student.grade import grade
from student.attendance import eligible

a = int(input("Enter marks of subject 1: "))
b = int(input("Enter marks of subject 2: "))
c = int(input("Enter marks of subject 3: "))

attendance = float(input("Enter attendance percentage: "))

t = total(a, b, c)
p = percentage(t)

print("Total:", t)
print("Percentage:", p)
print("Grade:", grade(p))
print("Attendance:", eligible(attendance))