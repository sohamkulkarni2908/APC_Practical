student = {"Siddhant", "Nikhil", "Nisarg", "Chetan", "Shubham"}

name = input("Enter the name to be checked: ")

if name in student:
    print(name, "is present in the set.")
else:
    print(name, "is not present in the set.")