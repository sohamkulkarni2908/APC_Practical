import re
text = input("Enter a sentence: ")
result = re.findall(r'\b\w{5}\b', text)
print("Words with exactly five characters:", result)
