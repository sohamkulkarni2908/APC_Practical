class BankAccount:
    def calculate_interest(self):
        print("Calculating interest")

class Savings(BankAccount):
    def calculate_interest(self):
        print("Savings Account Interest: 5%")

class Current(BankAccount):
    def calculate_interest(self):
        print("Current Account Interest: 2%")

class FixedDeposit(BankAccount):
    def calculate_interest(self):
        print("Fixed Deposit Interest: 7%")


accounts = [Savings(), Current(), FixedDeposit()]
for account in accounts:
    account.calculate_interest()