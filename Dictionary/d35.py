paragraph = input("Enter a paragraph: ")

words = paragraph.split()
result = {}

for word in words:
    length = len(word)
    result[length] = result.get(length, 0) + 1

print("Word length : Number of words")

for length, count in sorted(result.items()):
    print(length, ":", count)