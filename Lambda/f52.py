words = input("Enter words: ").split()

lengths = list(map(lambda word: len(word), words))
long_words = list(filter(lambda word: len(word) > 5, words))
sorted_words = sorted(words, key=lambda word: len(word))

print("Length of words:", lengths)
print("Words having more than 5 characters:", long_words)
print("Words sorted according to length:", sorted_words)