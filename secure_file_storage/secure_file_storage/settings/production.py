from .base import *
from os import environ
from django.core.exceptions import ImproperlyConfigured


def get_env_setting(setting):
    ''' Get the environment setting or return exception '''
    try:
        return environ[setting]
    except KeyError:
        raise ImproperlyConfigured(f'Set the {setting} env variable')


SECRET_KEY = get_env_setting('SECRET_KEY')

ALLOWED_HOSTS += ['lamkashingpaul.com']

WSGI_APPLICATION = 'secure_file_storage.wsgi.application'
