class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Doctor(Person):
    def __init__(self, name, age, specialization):
        Person.__init__(self, name, age)
        self.specialization = specialization

    def display_doctor(self):
        print("Doctor Name:", self.name)
        print("Age:", self.age)
        print("Specialization:", self.specialization)


class Patient(Person):
    def __init__(self, name, age, disease):
        Person.__init__(self, name, age)
        self.disease = disease

    def display_patient(self):
        print("Patient Name:", self.name)
        print("Age:", self.age)
        print("Disease:", self.disease)


class Surgeon(Doctor, Patient):
    def __init__(self, name, age, specialization, disease):
        Doctor.__init__(self, name, age, specialization)
        self.disease = disease

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Specialization:", self.specialization)
        print("Disease:", self.disease)


class MedicalResearcher(Doctor):
    def research(self):
        print("Medical Researcher is conducting research")


surgeon = Surgeon("Dr. Soham", 35, "Cardiology", "Heart Disease")
researcher = MedicalResearcher("Dr. Nikhil", 40, "Neurology")

print("Surgeon:")
surgeon.display()
print()
print("Medical Researcher:")
researcher.display_doctor()
researcher.research()