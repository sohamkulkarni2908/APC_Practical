from abc import ABC, abstractmethod
class Authentication(ABC):
    @abstractmethod
    def authenticate(self):
        pass

class Password(Authentication):
    def authenticate(self):
        print("Authentication using Password")

class OTP(Authentication):
    def authenticate(self):
        print("Authentication using OTP")

class Biometric(Authentication):
    def authenticate(self):
        print("Authentication using Biometric")

p = Password()
o = OTP()
b = Biometric()
p.authenticate()
o.authenticate()
b.authenticate()