numb = (10, 20, 10, 30, 20, 10, 20)
f = {}

for num in numb:
    if num in f:
        f[num] = f[num] + 1
    else:
        f[num] = 1

for num in f:
    print("Frequency of number : ",num, "=", f[num])