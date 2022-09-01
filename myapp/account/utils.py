from django.core.mail import EmailMessage
import os

class Utils:
    @staticmethod
    def Send_email(data):
        email = EmailMessage(
            subject=data['subject'],
            body=data['body'],
            from_email=os.environ.get('EMAIL_FORM'),
            to = [data ['to_email']]
        )
        email.send()