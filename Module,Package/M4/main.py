import string_utils

s = input("Enter a string: ")
print("Vowels:", string_utils.vowels(s))
print("Reverse:", string_utils.reverse(s))
print("Words:", string_utils.words(s))
print("Without spaces:", string_utils.remove_spaces(s))

if string_utils.palindrome(s):
    print("Palindrome")
else:
    print("Not Palindrome")