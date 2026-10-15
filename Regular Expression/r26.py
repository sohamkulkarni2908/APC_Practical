import re
text = input("Enter research paper references: ")
doi = re.findall(r'10\.\d{4,9}/\S+', text)
years = re.findall(r'\b(?:19|20)\d{2}\b', text)
emails = re.findall(r'[\w.-]+@[\w.-]+\.[A-Za-z]{2,}', text)
urls = re.findall(r'https?://\S+', text)

print("DOI:", doi)
print("Publication years:", years)
print("Email addresses:", emails)
print("URLs:", urls)