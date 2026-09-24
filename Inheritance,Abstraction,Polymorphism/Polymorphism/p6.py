class Student:
    def calculate_grade(self):
        print("Calculating grade")

class Engineering(Student):
    def calculate_grade(self):
        print("Engineering Grade: A")

class Medical(Student):
    def calculate_grade(self):
        print("Medical Grade: A")

class Management(Student):
    def calculate_grade(self):
        print("Management Grade: A")

students = [Engineering(), Medical(), Management()]
for student in students:
    student.calculate_grade()