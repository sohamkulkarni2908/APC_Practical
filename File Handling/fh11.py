f = open("student.txt", "r")
data = f.read()
words = data.split()
longest = ""

for word in words:
    if len(word) > len(longest):
        longest = word

print("Longest word:", longest)
f.close()