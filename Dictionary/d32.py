numbers = [2, 7, 11, 15, 3]
target = 9

seen = {}

for num in numbers:
    required = target - num

    if required in seen:
        print("Numbers:", required, num)
        break

    seen[num] = True