class Employee:
    def __init__(self, emp_id, name, salary):
        self.emp_id = emp_id
        self.name = name
        self.salary = salary

    def display_employee(self):
        print("Employee ID:", self.emp_id)
        print("Name:", self.name)
        print("Salary:", self.salary)

class Manager(Employee):
    def __init__(self, emp_id, name, salary, department):
        super().__init__(emp_id, name, salary)
        self.department = department

    def display_manager(self):
        self.display_employee()
        print("Department:", self.department)

    def annual_salary(self):
        return self.salary * 12


manager = Manager(101, "Soham", 50000, "IT")
manager.display_manager()
print("Annual Salary:", manager.annual_salary())