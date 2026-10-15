import re
password = input("Enter a password: ")
pattern = r'(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@#$%&*!]).{8,}'

if re.fullmatch(pattern, password):
    print("Valid password")
else:
    print("Invalid password")