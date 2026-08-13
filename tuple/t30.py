patients = (
    (1, "Prathamesh", 25, "O+ve"),
    (2, "Shrirang", 30, "A+ve"),
    (3, "Atharv", 35, "B+ve"),
    (4, "Nikhil", 18, "O+ve")
)

print("All Patient records:")
for p in patients:
    print("ID:", p[0], "Name:", p[1], "Age:", p[2], "Blood Group:", p[3])

search_id = int(input("Enter patient ID to search: "))
for p in patients:
    if p[0] == search_id:
        print("Patient found:", p)

print("Total patients =", len(patients))
blood_group = input("Enter blood group to filter: ")
print("Patients with blood group", blood_group, ":")
for p in patients:
  if p[3] == blood_group:
     print(p)