f1 = open("file1.txt", "r")
f2 = open("file2.txt", "r")

line_no = 0
same = True
while True:
    line1 = f1.readline()
    line2 = f2.readline()

    if line1 == "" and line2 == "":
        break

    line_no = line_no + 1
    if line1 != line2:
        print("Files are different")
        print("First difference at line:", line_no)
        same = False
        break

if same:
    print("Files are identical")

f1.close()
f2.close()