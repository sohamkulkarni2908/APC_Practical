class Patient:
    def __init__(self, patient_id, name, age, disease, consultation_fee):
        self.patient_id = patient_id
        self.name = name
        self.age = age
        self.disease = disease
        self.consultation_fee = consultation_fee

    def display(self):
        print("Patient ID:", self.patient_id)
        print("Name:", self.name)
        print("Age:", self.age)
        print("Disease:", self.disease)
        print("Consultation Fee:", self.consultation_fee)

    def total_bill(self, medicine_fee):
        return self.consultation_fee + medicine_fee


p = Patient(101, "Soham", 20, "Fever", 500)
p.display()
medicine_fee = 1000
print("Total Bill:", p.total_bill(medicine_fee))