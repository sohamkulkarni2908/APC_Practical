from texttools.cleaning import clean
from texttools.tokenization import tokenize
from texttools.frequency import frequency

text = input("Enter text: ")

text = clean(text)

words = tokenize(text)

print("Clean text:", text)
print("Words:", words)
print("Frequency:", frequency(words))