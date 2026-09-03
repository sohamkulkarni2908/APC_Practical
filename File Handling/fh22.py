f1 = open("file1.txt", "r")
f2 = open("file2.txt", "r")
f3 = open("file3.txt", "w")

data1 = f1.read()
data2 = f2.read()

f3.write(data1)
f3.write("\n")
f3.write(data2)

f1.close()
f2.close()
f3.close()
print("Files merged successfully")