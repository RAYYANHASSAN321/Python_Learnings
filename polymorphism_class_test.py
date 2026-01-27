class Notification:
    def send_notification(self, message):
        pass


class EmailNotification(Notification):
    def send_notification(self, message):
        print(f"Email sent: {message}")


class SMSNotification(Notification):
    def send_notification(self, message):
        print(f"SMS sent: {message}")


class PushNotification(Notification):
    def send_notification(self, message):
        print(f"Push notification sent: {message}")

notifications = [
    EmailNotification(),
    SMSNotification(),
    PushNotification()
]

message = "Your order has been shipped!"

for notify in notifications:
    notify.send_notification(message)
