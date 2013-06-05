from .settings_base import *


# Setup a sqlite database for local deployment

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': path.join(PROJECT_ROOT, 'mycms.db'),
    }
}