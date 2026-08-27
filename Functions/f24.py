balance = 0
transactions = []


def deposit(amount):
    global balance

    balance += amount
    transactions.append("Deposited: " + str(amount))
    print("Amount deposited successfully.")


def withdrawal(amount):
    global balance

    if amount <= balance:
        balance -= amount
        transactions.append("Withdrawn: " + str(amount))
        print("Amount withdrawn successfully.")
    else:
        print("Insufficient balance.")


def balance_enquiry():
    print("Current Balance:", balance)


def transaction_history():
    print("\nTransaction History:")

    if len(transactions) == 0:
        print("No transactions.")
    else:
        for transaction in transactions:
            print(transaction)


while True:
    print("\n1. Deposit")
    print("2. Withdrawal")
    print("3. Balance Enquiry")
    print("4. Transaction History")
    print("5. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        amount = float(input("Enter amount: "))
        deposit(amount)

    elif choice == 2:
        amount = float(input("Enter amount: "))
        withdrawal(amount)

    elif choice == 3:
        balance_enquiry()

    elif choice == 4:
        transaction_history()

    elif choice == 5:
        break

    else:
        print("Invalid choice")