class BankAccount:
    def __init__(self, account_no, balance):
        self.account_no = account_no
        self.balance = balance

    def display_account(self):
        print("Account No:", self.account_no)
        print("Balance:", self.balance)

class SavingsAccount(BankAccount):
    def calculate_interest(self, rate):
        return self.balance * rate / 100

class PremiumSavingsAccount(SavingsAccount):
    def display_benefits(self):
        print("Benefits: Higher Interest and Premium Services")


account = PremiumSavingsAccount(101, 50000)
account.display_account()
interest = account.calculate_interest(5)
print("Interest:", interest)
account.display_benefits()