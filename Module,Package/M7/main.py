from mathutils.basic import add, subtract, multiply
from mathutils.number import prime, palindrome, armstrong
from mathutils.statistics import mean, maximum, minimum

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

print("Addition:", add(a, b))
print("Subtraction:", subtract(a, b))
print("Multiplication:", multiply(a, b))

print("Mean:", mean(a, b, c))
print("Maximum:", maximum(a, b, c))
print("Minimum:", minimum(a, b, c))

print("Prime:", prime(a))
print("Palindrome:", palindrome(a))
print("Armstrong:", armstrong(a))