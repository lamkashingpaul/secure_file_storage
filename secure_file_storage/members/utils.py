from django.core.exceptions import ImproperlyConfigured
from os import environ
from twilio.rest import Client


def get_env_setting(setting):
    ''' Get the environment setting or return exception '''
    try:
        return environ[setting]
    except KeyError:
        raise ImproperlyConfigured(f'Set the {setting} env variable')


account_sid = get_env_setting('TWILIO_ACCOUNT_SID')
auth_token = get_env_setting('TWILIO_AUTH_TOKEN')
from_phone = get_env_setting('FROM_PHONE')

client = Client(account_sid, auth_token)


def send_sms(user_code, phone_number):
    message = client.messages.create(body=f'Hi! Your user and verification code is {user_code}',
                                     from_=f'{from_phone}',
                                     to=f'{phone_number}',
                                     )

    print(message.sid)
