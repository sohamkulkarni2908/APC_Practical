f = open("records.txt", "r")
next(f)
students = []

for line in f:
    data = line.strip().split(",")
    students.append(data)

print("All Records:")

for s in students:
    print(s)

highest = students[0]

for s in students:
    if int(s[2]) > int(highest[2]):
        highest = s

print("Highest Marks:", highest[1])
total = 0

for s in students:
    total = total + int(s[2])

average = total / len(students)
print("Average Marks:", average)
print("Students scoring more than 80:")

for s in students:
    if int(s[2]) > 80:
        print(s[1])

f.close()