f = open("student.txt", "r")
lines = f.readlines()
lines.reverse()
for line in lines:
    print(line, end="")

f.close()