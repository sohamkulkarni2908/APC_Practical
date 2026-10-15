import re
text = input("Enter a paragraph: ")
urls = re.findall(r'https?://\S+', text)
print("Web addresses:", urls)