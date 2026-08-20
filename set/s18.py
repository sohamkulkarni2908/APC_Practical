sentence = input("Enter a sentence: ")

words = set(sentence.split())

print("Unique words:")
for w in words:
    print(w)