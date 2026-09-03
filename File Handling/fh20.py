f = open("transactions.txt", "r")
deposit = 0
withdrawal = 0
balance = 0
largest = 0

for line in f:
    data = line.strip().split(",")

    type = data[0]
    amount = int(data[1])

    if type == "deposit":
        deposit = deposit + amount
        balance = balance + amount
    else:
        withdrawal = withdrawal + amount
        balance = balance - amount

    if amount > largest:
        largest = amount

print("Total deposits:", deposit)
print("Total withdrawals:", withdrawal)
print("Final balance:", balance)
print("Largest transaction:", largest)
f.close()