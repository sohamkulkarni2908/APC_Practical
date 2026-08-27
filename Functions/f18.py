def calculate_result(marks):
    total = sum(marks)
    percentage = total / 5

    if percentage >= 90:
        grade = "A"
    elif percentage >= 75:
        grade = "B"
    elif percentage >= 60:
        grade = "C"
    elif percentage >= 50:
        grade = "D"
    else:
        grade = "Fail"

    return percentage, grade

marks = []
for i in range(5):
    marks.append(float(input("Enter marks: ")))

percentage, grade = calculate_result(marks)
print("Percentage:", percentage)
print("Grade:", grade)