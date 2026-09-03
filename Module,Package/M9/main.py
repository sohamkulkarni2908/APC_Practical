from banking.account import create_account
from banking.transaction import deposit, withdraw
from banking.loan import loan_amount

name = input("Enter name: ")
balance = int(input("Enter initial balance: "))

create_account(name, balance)

d = int(input("Enter deposit amount: "))
balance = deposit(balance, d)

print("Balance after deposit:", balance)

w = int(input("Enter withdrawal amount: "))
balance = withdraw(balance, w)

print("Balance after withdrawal:", balance)

p = int(input("Enter loan amount: "))
r = float(input("Enter interest rate: "))
t = int(input("Enter time: "))

print("Loan amount with interest:", loan_amount(p, r, t))