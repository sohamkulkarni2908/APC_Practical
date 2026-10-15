import re
text = "Hello World\tPython\nProgramming"
result = re.findall(r'[ \t\n]', text)
print("Spaces, tabs, and newlines:", result)
print("Total count:", len(result))
