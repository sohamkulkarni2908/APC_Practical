class Employee:
    def __init__(self, name, basic_salary):
        self.name = name
        self.basic_salary = basic_salary

    def display(self):
        print("Name:", self.name)
        print("Basic Salary:", self.basic_salary)

class Manager(Employee):
    def calculate_salary(self):
        allowance = self.basic_salary * 0.30
        return self.basic_salary + allowance

class Developer(Employee):
    def calculate_salary(self):
        allowance = self.basic_salary * 0.20
        return self.basic_salary + allowance

class Tester(Employee):
    def calculate_salary(self):
        allowance = self.basic_salary * 0.15
        return self.basic_salary + allowance

manager = Manager("Ritesh", 50000)
developer = Developer("Nikhil", 40000)
tester = Tester("Soham", 30000)

manager.display()
print("Manager Total Salary:", manager.calculate_salary())
print()

developer.display()
print("Developer Total Salary:", developer.calculate_salary())
print()

tester.display()
print("Tester Total Salary:", tester.calculate_salary())