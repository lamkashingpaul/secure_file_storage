from .base import *

SECRET_KEY = os.environ['SECRET_KEY']

ALLOWED_HOSTS += ['lamkashingpaul.com']

WSGI_APPLICATION = 'secure_file_storage.wsgi.application'
