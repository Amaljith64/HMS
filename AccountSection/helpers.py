from django.conf import settings
from twilio.rest import Client

# Create your models here.


class MessageHandler:
    phone=None
    otp = None

    def __init__(self,phone,otp) -> None:
        self.phone = phone
        self.otp = otp

    def send_otp_via_message(self):
        client = Client(settings.ACCOUNT_SID,settings.AUTH_TOKEN)

        message = client.messages.create(
            body=f"Your OTP is: {self.otp}",
            from_=f'{settings.TWILIO_PHONE_NUMBER}',
            to=f'{settings.COUNTRY_CODE}{self.phone}'
        )
    

        print(message.sid)
        
