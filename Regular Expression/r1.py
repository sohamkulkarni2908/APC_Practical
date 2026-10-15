import re
text = "My roll number is 73 and my marks are 85"
result = re.findall(r'\d', text)
print("Digits:", result)
