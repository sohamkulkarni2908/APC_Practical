def count_element(numbers, element):
    count = 0

    for num in numbers:
        if num == element:
            count += 1
    return count

numbers = list(map(int, input("Enter numbers: ").split()))
element = int(input("Enter element: "))
print("Occurrences:", count_element(numbers, element))