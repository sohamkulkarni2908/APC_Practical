class Student:
    def __init__(self, name, roll_no):
        self.name = name
        self.roll_no = roll_no

class Result(Student):
    def __init__(self, name, roll_no, m1, m2, m3):
        super().__init__(name, roll_no)
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    def calculate_result(self):
        total = self.m1 + self.m2 + self.m3
        percentage = total / 3

        if percentage >= 75:
            grade = "A"
        elif percentage >= 60:
            grade = "B"
        elif percentage >= 50:
            grade = "C"
        else:
            grade = "D"

        print("Name:", self.name)
        print("Roll No:", self.roll_no)
        print("Total Marks:", total)
        print("Percentage:", percentage)
        print("Grade:", grade)


result = Result("Soham", 101, 80, 75, 90)
result.calculate_result()