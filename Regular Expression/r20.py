import re
text = input("Enter filenames: ")
extensions = re.findall(r'\.([a-zA-Z0-9]+)\b', text)
print("File extensions:", extensions)