def unique_elements(numbers):
    result = []
    for num in numbers:
        if num not in result:
            result.append(num)
    return result

numbers = list(map(int, input("Enter numbers: ").split()))
print("Unique elements:", unique_elements(numbers))
