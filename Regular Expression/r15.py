import re
text = input("Enter a social media post: ")
hashtags = re.findall(r'#\w+', text)
print("Hashtags:", hashtags)