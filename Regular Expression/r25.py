import re

text = input("Enter student details: ")
names = re.findall(r'Name:\s*([A-Za-z ]+)', text)
roll_numbers = re.findall(r'Roll:\s*(\d+)', text)
marks = re.findall(r'Marks:\s*(\d+)', text)

print("Student names:", names)
print("Roll numbers:", roll_numbers)
print("Marks:", marks)