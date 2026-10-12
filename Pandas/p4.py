import pandas as pd

data = {
    "Patient ID" : [1,2,3,4,5],
    "Name" : ["Rehan","Nisarg","Nikhil","Ritesh","Chetan"],
    "Age": [20,22,25,23,61],
    "Disease": ["Fever", "Cold", "Headache", "Fever","Cough"],
    "Charges" : [20000,8000,15000,20000,80000] 
}

df = pd.DataFrame(data)

print("Patients Above age 60: ")
print(df[df["Age"] > 60])
print()

print("Average medical charges: ")
print(df["Charges"].mean())
print()

print("Maximum medical charge: ")
print(df["Charges"].max())
print()

print("Patients having medical charge above 50000: ")
print(df[df["Charges"] > 50000])