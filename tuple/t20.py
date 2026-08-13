numbers = (10, 20, 30, 40, 50, 60)
num = int(input("Enter number to search: "))

if num in numbers:
    print("Number found in tuple")
else:
    print("Number not found in tuple")