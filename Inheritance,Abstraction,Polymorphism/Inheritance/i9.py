class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Student(Person):
    def __init__(self, name, age, roll_no):
        self.name = name
        self.age = age
        self.roll_no = roll_no

    def display_student(self):
        print("Student Name:", self.name)
        print("Age:", self.age)
        print("Roll No:", self.roll_no)


class Faculty(Person):
    def __init__(self, name, age, subject):
        self.name = name
        self.age = age
        self.subject = subject

    def display_faculty(self):
        print("Faculty Name:", self.name)
        print("Age:", self.age)
        print("Subject:", self.subject)


class TeachingAssistant(Student, Faculty):
    def __init__(self, name, age, roll_no, subject):
        Student.__init__(self, name, age, roll_no)
        self.subject = subject

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Roll No:", self.roll_no)
        print("Subject:", self.subject)


ta = TeachingAssistant("Soham", 20, 101, "Python")

ta.display()