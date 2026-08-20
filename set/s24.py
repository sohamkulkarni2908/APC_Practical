day1 = {101, 102, 103, 104, 105}
day2 = {103, 104, 105, 106, 107}

print("Unique visitors:", day1 | day2)
print("Returning visitors:", day1 & day2)
print("Only 1st day:", day1 - day2)
print("Only 2nd day:", day2 - day1)



category1 = {"Laptop", "Mouse", "Keyboard", "Monitor"}
category2 = {"Keyboard", "Monitor", "Printer", "Scanner", "Headphones"}

common = category1 & category2

print("Products in both categories:", common)