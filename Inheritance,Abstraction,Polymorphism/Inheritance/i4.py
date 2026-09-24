class PersonalDetails:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class ProfessionalDetails:
    def __init__(self, job, salary):
        self.job = job
        self.salary = salary

class Employee(PersonalDetails, ProfessionalDetails):
    def __init__(self, name, age, job, salary):
        PersonalDetails.__init__(self, name, age)
        ProfessionalDetails.__init__(self, job, salary)

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Job:", self.job)
        print("Salary:", self.salary)

employee = Employee("Soham", 20, "Software Developer", 50000)
employee.display()