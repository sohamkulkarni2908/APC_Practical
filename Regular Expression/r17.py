import re
text = input("Enter a sentence: ")
pattern = r'\b(\w+)\s+\1\b'
result = re.findall(pattern, text, re.IGNORECASE)
print("Repeated words:", result)