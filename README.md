hax10m.com
==========

This is the source code for hax10m.com. The site currently runs on Django and uses Django-cms and is configured for deployment on Heroku.

Follow these steps if you want to deploy a copy of this site on Heroku.

1. Clone this repository

    $ git clone git://github.com/menglewis/hax10m.com.git

2. Sign-Up for a Heroku account. https://api.heroku.com/signup

3. Install the Heroku client. http://devcenter.heroku.com/articles/quickstart

4. Login to Heroku on your Heroku toolbelt

    $ heroku login

5. Create your Heroku application

    $ heroku create --stack cedar

6. Push the code to Heroku

    $ git push heroku master

7. Set your Django Secret key in the Heroku environment

    $ heroku config:add SECRET_KEY=enter_a_secret_key_here

8. Sync the database and create an admin account

    $ heroku run python manage.py syncdb --all

9. Run database migrations

    $ heroku run python manage.py migrate --fake

10. (Optional) Rename your heroku application

    $ heroku apps:rename NEWNAME

11. Open your Heroku application in the browser and have fun!

    $ heroku open

