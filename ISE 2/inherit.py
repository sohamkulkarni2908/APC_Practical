class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

class Employee(Person):
    def __init__ (self,name,age,id,salary):
        self.name = name
        self.age = age
        self.id = id
        self.salary = salary


class Manager(Employee):
    def __init__(self,name,age,id,salary,dept,size):
         self.name = name
         self.age = age
         self.id = id
         self.salary = salary
         self.dept = dept
         self.size = size

    def display(self):
        print("Employee Details:")
        print()
        print("name:",self.name)
        print("age:",self.age)
        print("id:",self.id)
        print("salary:",self.salary)
        print("Manager:")
        print("Department:",self.dept)
        print("Team size:",self.size)


obj = Manager("Soham",21,101,25000,"IT",5)
obj.display()