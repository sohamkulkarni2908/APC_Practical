import re
text = input("Enter a sentence: ")
result = re.sub(r' +', ' ', text)
print("After replacing spaces:")
print(result)
