def count_vowels(text):
    cnt = 0

    for char in text:
        if char.lower() in "aeiou":
            cnt += 1
    return cnt

text = input("Enter a string: ")
print("Number of vowels:", count_vowels(text))