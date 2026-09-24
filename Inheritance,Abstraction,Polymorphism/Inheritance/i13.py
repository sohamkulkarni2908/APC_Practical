class Printer:
    def print_document(self):
        print("Printing document...")

class Scanner:
    def scan_document(self):
        print("Scanning document...")

class MultifunctionDevice(Printer, Scanner):
    def display(self):
        print("Multifunction Device")


device = MultifunctionDevice()
device.display()
device.scan_document()
device.print_document()
