f = open("student.txt", "r")
data = f.read()

old_word = input("Enter word to replace: ")
new_word = input("Enter new word: ")
data = data.replace(old_word, new_word)
f.close()

f = open("student.txt", "w")
f.write(data)
f.close()
print("Word replaced successfully")