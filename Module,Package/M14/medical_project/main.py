from Patient.patient import patient_details
from Doctor.doctor import doctor_details
from Billing.bill import calculate_bill
from MedicalRecords.records import medical_record

print("MEDICAL MANAGEMENT SYSTEM")
patient_details()
doctor_details()
calculate_bill(5000)
medical_record()