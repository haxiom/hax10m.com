from .settings_base import *
import dj_database_url

DEBUG = False


# Using a real webserver for deployment
INSTALLED_APPS += ('gunicorn',)

# settings for Heroku Postgres DB
DATABASES['default'] = dj_database_url.config(default='postgres://localhost')