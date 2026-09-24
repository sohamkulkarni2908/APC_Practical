from abc import ABC, abstractmethod
class Appointment(ABC):
    @abstractmethod
    def book_appointment(self):
        pass

    @abstractmethod
    def calculate_fee(self):
        pass

class General(Appointment):

    def book_appointment(self):
        print("General appointment booked")

    def calculate_fee(self):
        return 500

class Specialist(Appointment):

    def book_appointment(self):
        print("Specialist appointment booked")

    def calculate_fee(self):
        return 1000

class Emergency(Appointment):

    def book_appointment(self):
        print("Emergency appointment booked")

    def calculate_fee(self):
        return 2000

a1 = General()
a2 = Specialist()
a3 = Emergency()
a1.book_appointment()
print("Fee:", a1.calculate_fee())
a2.book_appointment()
print("Fee:", a2.calculate_fee())
a3.book_appointment()
print("Fee:", a3.calculate_fee())