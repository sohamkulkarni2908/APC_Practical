from abc import ABC, abstractmethod
class Patient(ABC):
    @abstractmethod
    def calculate_bill(self):
        pass

    @abstractmethod
    def treatment(self):
        pass

class InPatient(Patient):
    def calculate_bill(self):
        print("In-Patient Bill: 10000")

    def treatment(self):
        print("Treatment: Hospital Admission")

class OutPatient(Patient):
    def calculate_bill(self):
        print("Out-Patient Bill: 3000")

    def treatment(self):
        print("Treatment: Regular Check-up")

class Emergency(Patient):
    def calculate_bill(self):
        print("Emergency Bill: 15000")

    def treatment(self):
        print("Treatment: Emergency Care")

patients = [InPatient(), OutPatient(), Emergency()]
for patient in patients:
    patient.calculate_bill()
    patient.treatment()