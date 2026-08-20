marks = {"Soham": 80,"Siddhant": 75,"Nikhil": 90}

name = input("Enter student name: ")
new_marks = int(input("Enter new marks: "))

if name in marks:
    marks[name] = new_marks
    print(marks)
else:
    print("Student not found")