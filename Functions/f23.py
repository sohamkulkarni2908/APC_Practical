def total_marks(marks):
    return sum(marks)


def percentage(total):
    return total / 5


def grade(per):
    if per >= 90:
        return "A"
    elif per >= 75:
        return "B"
    elif per >= 60:
        return "C"
    elif per >= 50:
        return "D"
    else:
        return "F"


students = {}

n = int(input("Enter number of students: "))

for i in range(n):
    name = input("Enter student name: ")
    roll = int(input("Enter roll number: "))

    marks = []
    for j in range(5):
        mark = float(input("Enter marks: "))
        marks.append(mark)

    students[roll] = {
        "name": name,
        "marks": marks
    }

print("\nStudent Records")

total_class = 0
highest = None
lowest = None

for roll, data in students.items():
    total = total_marks(data["marks"])
    per = percentage(total)
    g = grade(per)

    print("\nName:", data["name"])
    print("Roll No:", roll)
    print("Total:", total)
    print("Percentage:", per)
    print("Grade:", g)

    total_class += per

    if highest is None or per > highest[0]:
        highest = (per, data["name"])

    if lowest is None or per < lowest[0]:
        lowest = (per, data["name"])

class_average = total_class / len(students)

print("\nClass Average:", class_average)
print("Highest Scorer:", highest[1], highest[0])
print("Lowest Scorer:", lowest[1], lowest[0])