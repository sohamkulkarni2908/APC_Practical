class Employee:
    def calculate_salary(self):
        return 0

class Manager(Employee):
    def calculate_salary(self):
        return 50000 + 20000

class Developer(Employee):
    def calculate_salary(self):
        return 40000 + 10000

class Tester(Employee):
    def calculate_salary(self):
        return 30000 + 5000

employees = [
    Manager(),
    Developer(),
    Tester()
]
for employee in employees:
    print("Salary:", employee.calculate_salary())