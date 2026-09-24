class Student:
    def __init__(self, roll_no, name, marks):
        self.roll_no = roll_no
        self.name = name
        self.marks = marks

    def display(self):
        total = sum(self.marks)
        percentage = total / len(self.marks)

        print("Roll No:", self.roll_no)
        print("Name:", self.name)
        print("Marks:", self.marks)
        print("Percentage:", percentage)
        print()

s1 = Student(1, "Soham", [80, 75, 90])
s2 = Student(2, "Nikhil", [70, 85, 80])
s3 = Student(3, "Ritesh", [90, 95, 85])
s1.display()
s2.display()
s3.display()