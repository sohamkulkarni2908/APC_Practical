import re
text = input("Enter a string: ")
result = re.sub(r'[^a-zA-Z0-9 ]', '', text)

print("After removing special characters:")
print(result)