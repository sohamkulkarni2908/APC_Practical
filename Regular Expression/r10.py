import re
text = input("Enter a sentence: ")
words = re.findall(r'\b\w+\b', text)

print("Words:", words)
print("Number of words:", len(words))
