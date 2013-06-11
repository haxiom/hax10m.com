from .base import *
import dj_database_url

DEBUG = False

INSTALLED_APPS += ('gunicorn',)

# settings for Heroku Postgres DB
DATABASES['default'] = dj_database_url.config(default='postgres://localhost')
