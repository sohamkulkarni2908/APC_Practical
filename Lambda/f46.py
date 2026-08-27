words = input("Enter words: ").split()
result = sorted(words, key=lambda word: len(word))
print("Sorted words:", result)