f = open("attendance.txt", "r")
for line in f:
    data = line.strip().split(",")
    roll = data[0]
    name = data[1]
    present = int(data[2])
    total = int(data[3])

    percentage = (present / total) * 100
    print(name, "Attendance:", percentage, "%")

    if percentage < 75:
        print(name, "has attendance below 75%")

f.close()