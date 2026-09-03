import student

m1 = int(input("Enter marks of subject 1: "))
m2 = int(input("Enter marks of subject 2: "))
m3 = int(input("Enter marks of subject 3: "))
t = student.total(m1, m2, m3)
p = student.percentage(t)
g = student.grade(p)

print("Total:", t)
print("Percentage:", p)
print("Grade:", g)