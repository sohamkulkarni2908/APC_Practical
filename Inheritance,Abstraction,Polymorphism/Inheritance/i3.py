class Academic:
    def __init__(self, academic_marks):
        self.academic_marks = academic_marks

class Sports:
    def __init__(self, sports_marks):
        self.sports_marks = sports_marks

class Student(Academic, Sports):
    def __init__(self, name, academic_marks, sports_marks):
        Academic.__init__(self, academic_marks)
        Sports.__init__(self, sports_marks)
        self.name = name

    def display(self):
        print("Name:", self.name)
        print("Academic Marks:", self.academic_marks)
        print("Sports Marks:", self.sports_marks)

    def overall_performance(self):
        return (self.academic_marks + self.sports_marks) / 2


student = Student("Soham", 80, 70)
student.display()
print("Overall Performance:", student.overall_performance())