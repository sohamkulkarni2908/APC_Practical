f = open("student.txt", "r")
data = f.readlines()
cnt = 0
for line in data:
    cnt += 1
print("Total number of lines in the file:", cnt)