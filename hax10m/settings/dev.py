from .base import *


# Setup a sqlite database for local deployment

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': join(PROJECT_ROOT, 'haxiom.db'),
    }
}
