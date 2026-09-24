class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Student(Person):
    def __init__(self, name, age, roll_no, course):
        super().__init__(name, age)
        self.roll_no = roll_no
        self.course = course

class ResearchStudent(Student):
    def __init__(self, name, age, roll_no, course, research_topic, guide):
        super().__init__(name, age, roll_no, course)
        self.research_topic = research_topic
        self.guide = guide

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Roll No:", self.roll_no)
        print("Course:", self.course)
        print("Research Topic:", self.research_topic)
        print("Guide:", self.guide)

student = ResearchStudent(
    "Soham", 20, 101, "B.Tech",
    "Artificial Intelligence", "Dr. Sharma"
)
student.display()