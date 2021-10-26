import os
from .json_reader import json_settings
import django_heroku

settings = json_settings()

__STATIC_PATH = os.path.dirname(os.path.dirname(__file__))

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(__STATIC_PATH, 'staticfiles')
django_heroku.settings(locals())