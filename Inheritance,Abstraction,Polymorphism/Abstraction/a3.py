from abc import ABC, abstractmethod
class BankAccount(ABC):
    @abstractmethod
    def deposit(self, amount):
        pass

    @abstractmethod
    def withdraw(self, amount):
        pass

class Savings(BankAccount):
    def deposit(self, amount):
        print("Deposited:", amount)

    def withdraw(self, amount):
        print("Withdrawn:", amount)

class Current(BankAccount):
    def deposit(self, amount):
        print("Deposited:", amount)

    def withdraw(self, amount):
        print("Withdrawn:", amount)


savings = Savings()
current = Current()
savings.deposit(5000)
savings.withdraw(2000)
current.deposit(10000)
current.withdraw(3000)