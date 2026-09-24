class Notification:
    def send(self):
        print("Sending notification")

class Email(Notification):
    def send(self):
        print("Sending Email")

class SMS(Notification):
    def send(self):
        print("Sending SMS")

class Push(Notification):
    def send(self):
        print("Sending Push Notification")

notifications = [Email(), SMS(), Push()]
for notification in notifications:
    notification.send()