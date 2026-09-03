import number_utils

n = int(input("Enter a number: "))

if number_utils.prime(n):
    print("Prime")
else:
    print("Not Prime")

if number_utils.palindrome(n):
    print("Palindrome")
else:
    print("Not Palindrome")

if number_utils.armstrong(n):
    print("Armstrong")
else:
    print("Not Armstrong")

if number_utils.perfect(n):
    print("Perfect")
else:
    print("Not Perfect")