hax10m.com
==========

This is the source code for hax10m.com. The site currently runs on Django and uses Django-cms and is configured for deployment on Heroku.

### Initial setup

```bash
## Clone this repository
$ git clone git://github.com/haxiom/hax10m.com.git

## Enter the project root
$ cd hax10m.com

## Setup virtualenv
$ virtualenv venv

## Activate virtualenv
$ source venv/bin/activate

## Install dependencies
$ pip install -r requirements.txt

## Setup the database and run initial migrations
$ python manage.py syncdb --all
$ python manage.py migrate --fake

## Run the local server
$ python manage.py runserver
```

### Deployment on Heroku
If you want to deploy to Heroku, start off by signing up for a Heroku account: https://id.heroku.com/signup and then download the Heroku toolbelt: http://devcenter.heroku.com/articles/quickstart.

Once you have the Heroku tools setup follow these steps to deploy.

```bash
## Login to Heroku
$ heroku login

## Create a new Heroku application
$ heroku create --stack cedar

## Push your code to Heroku
$ git push heroku master

## Set your Django Secret Key in the Heroku environment
$ heroku config:add SECRET_KEY=enter_a_secret_key_here

## Set Django Settings to point to Production Settings
$ heroku config:set DJANGO_SETTINGS_MODULE=hax10m.settings.production

## Sync the database and create an admin account
$ heroku run python manage.py syncdb --all

## Run database migrations
$ heroku run python manage.py migrate --fake

## (Optional) Rename your heroku application
$ heroku apps:rename NEWNAME

## Open your Heroku application in the browser and have fun!
$ heroku open
```

