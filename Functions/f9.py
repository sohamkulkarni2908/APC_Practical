def largest(numbers):
    large = numbers[0]

    for num in numbers:
        if num > large:
            large = num
    return large

numbers = list(map(int, input("Enter numbers: ").split()))
print("Largest:", largest(numbers))