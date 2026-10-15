import re
text = input("Enter invoice text: ")
invoice = re.findall(r'INV-\d+', text)
dates = re.findall(r'\d{2}-\d{2}-\d{4}', text)
amounts = re.findall(r'₹\s*\d+(?:,\d{3})*(?:\.\d{2})?', text)

print("Invoice number:", invoice)
print("Date:", dates)
print("Amount:", amounts)