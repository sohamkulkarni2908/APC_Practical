f = open("student.txt", "r")
data = f.read()
words = data.split()
count = {}

for word in words:
    if word in count:
        count[word] = count[word] + 1
    else:
        count[word] = 1

print(count)
f.close()