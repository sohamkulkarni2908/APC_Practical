import re
text = input("Enter a sentence: ")
result = re.findall(r'\b\w+s\b', text)
print("Words ending with s:", result)
