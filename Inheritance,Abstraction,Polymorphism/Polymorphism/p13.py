class Person:
    def display_role(self):
        print("Person")

class Student(Person):
    def display_role(self):
        print("Student")

class Faculty(Person):
    def display_role(self):
        print("Faculty")

class Admin(Person):
    def display_role(self):
        print("Admin")

people = [Student(), Faculty(), Admin()]
for person in people:
    person.display_role()