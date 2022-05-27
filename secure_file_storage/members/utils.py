from twilio.rest import Client
import os


account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']
from_phone = os.environ['FROM_PHONE']

client = Client(account_sid, auth_token)


def send_sms(user_code, phone_number):
    message = client.messages.create(body=f'Hi! Your user and verification code is {user_code}',
                                     from_=f'{from_phone}',
                                     to=f'{phone_number}',
                                     )

    print(message.sid)
