def display():
    f = open("employee.txt", "r")
    for line in f:
        print(line.strip())
    f.close()

def highest_salary():
    f = open("employee.txt", "r")
    highest = None
    for line in f:
        data = line.strip().split(",")
        salary = int(data[3])

        if highest is None or salary > int(highest[3]):
            highest = data

    print("Highest Paid Employee:", highest[1])
    print("Salary:", highest[3])
    f.close()

def average_salary():
    f = open("employee.txt", "r")
    total = 0
    count = 0

    for line in f:
        data = line.strip().split(",")
        total = total + int(data[3])
        count = count + 1

    print("Average Salary:", total / count)
    f.close()


def above_salary():
    amount = int(input("Enter salary: "))
    f = open("employee.txt", "r")

    for line in f:
        data = line.strip().split(",")

        if int(data[3]) > amount:
            print(data[1])

    f.close()


print("All Employees:")
display()
highest_salary()
average_salary()
above_salary()