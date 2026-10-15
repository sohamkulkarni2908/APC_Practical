import re
text = input("Enter a sentence: ")
result = re.findall(r'\b[Aa]\w*', text)
print("Words starting with A or a:", result)
