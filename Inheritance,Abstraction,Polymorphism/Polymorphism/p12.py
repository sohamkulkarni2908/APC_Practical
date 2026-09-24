class Payment:
    def make_payment(self):
        print("Making payment")

class UPI(Payment):
    def make_payment(self):
        print("Payment made using UPI")

class Card(Payment):
    def make_payment(self):
        print("Payment made using Card")

class Wallet(Payment):
    def make_payment(self):
        print("Payment made using Wallet")


def process_payment(payment):
    payment.make_payment()


upi = UPI()
card = Card()
wallet = Wallet()
process_payment(upi)
process_payment(card)
process_payment(wallet)