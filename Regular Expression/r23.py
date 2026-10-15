import re
text = input("Enter a Python comment: ")
comments = re.findall(r'#.*', text)
print("Single-line comments:", comments)