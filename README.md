## Fit Healthy Body 

It is a website that sell fitness equipment, nutrients plans to make your body heatlhty and be physically fit, exercise plans were you will follow a well devised plan on what type of exercise you have to do to target different parts of the body

#### For testing the following credentials can be used:

##### Member Login

Username: gitpod

Email: tinashechasakara@gmail.com

Password: 

Card payments

Card number: 4242 4242 4242 4242

Zip & CCV: any integer values are valid

### Wireframes 

[Wireframes](https://c14b6c1d-0386-44b5-9bef-ce64ddf62c2b.ws-eu03.gitpod.io/files/download/?id=1b302be3-2173-4eb5-9c35-2a3f7d52b49b)

## Technnologies used

### Languages used

##### HTML5
##### CSS3
##### JavaScript
#####  Python

### Frameworks, Libraries & Programs
Django

Python Web framework used to build the site.
Git

Git was used for version control by utilizing the Gitpod terminal to commit to Git and push to GitHub.
GitHub

GitHub is used to store the project code after being pushed from Git.
Heroku

Heroku is the app platform I deployed my project to.
Heroku Postgres

Heroku’s reliable and powerful database used to store the data for my deployed Heroku App.
jQuery:

A javascript library used to simplify DOM manipulation.
Bootstrap 4.5.3

Bootstrap was used to assist with the responsiveness and styling of the website using design templates.
Boto3

Python SDK for AWS, used to directly create, update, and delete AWS resources from my Python scripts.
gunicorn

WSGI server used to take care of everything happening between the web server and web application.
pillow

Python Imaging Library (PIL), used to add support for opening, manipulating, and saving images.
psycopg2

PostgreSQL database adapter

AWS

A cloud-based storage service used to store static and, media files.
Stripe

Stripe was used to deal with payments.

Temp Mail

Temp Mail was used to provide temporary, secure, anonymous, free, disposable email addresses for testing purposes.
Google fonts

Google fonts were used to import the fonts into the CSS file which is used on all pages throughout the project.


## Deployment

### Local Deployment

This project is deployed on heroku: 

In order to run this project locally on your own system, you need following:

Python3 to run the application
PIP to install all requirements
GIT for cloning and version control or you can just download the repo in zip format
IDE 

Clone the repo with command git clone https://github.com/chasakara/Fit-Healthy-Body.git or donwloand the zip file

Navigate to the correct file location after unpacking the files cd <path to folder>

Create .env with pipenv shell

Install all requirements with pip3 freeze > requirements.txt

launche the project python manage.py runserver

The Django server should be running locally now on http://127.0.0.1:8000/
When running the Django server for the first time, it should create a new SQLite3 database file: db.sqlite3

Run python manage.py makemigrations and python manage.py migrate

To have an access to Django Admin Panel, you must generate a superuser:
python manage.py createsuperuser

### Remote Deployment

1. Log in (or Register) to Heroku and from your dashboard click 'new' >        'create new app'.

2. Enter your 'App name' and choose the appropriate region, then click         'Create app'.

3. Then on the 'Resources' tab, search and add on the Heroku Postgres          database.

4. To use Postgres, install dj_database_url, and psycopg2 in the project       terminal using the following commands;

       $ pip3 install dj_database_url

       $ pip3 install psycopg2

5. Freeze the requirements to ensure Heroku installs all the apps              requirements when deployed using the following command;

        $ pip3 freeze > requirements.txt

6. To migrate to the Postgres, go to settings.py and add the following         import;

   import dj_database_url

7. Then down in the databases setting comment out the default configuration    and replace the default database with a call to dj_database_url.parse       and give it the database URL from Heroku.

   Config Vars

   Note: You can either get the database URL from your config variables in your app settings tab or from the command line by typing Heroku config.

7. Apply all migrations using the following command;

        $ python3 manage.py migrate

   After migrations have been applied amend your database configurations to;

   Config Vars

   Note: This will ensure that your Postgres database is used in deployment and your sqlite3 in development.

8. Create a superuser to log in with using the following command;

         $ python3 manage.py createsuperuser

9. Go to the Settings tab on Heroku, scroll to the 'Config Vars' section, and click 'Reveal Config Vars'.

    Config Vars

10. Enter the variables (key and value) contained in your environment           settings or stored in an env.py. The keys are listed below and values       are inputted by the user.

11. Install gunicorn using the following command;

        $ pip3 install gunicorn

    Then freeze into your requirements file.

12. Create a Procfile and add the following line;

    web: gunicorn fit-heatlhty-body.wsgi:application

    Note: The Procfile must be assigned a capital P.

13. Last, you need to temporarily disable collectstatic to ensure that          Heroku won't try to collect static files when we deploy. This is done       by adding the below variable;

|   DISABLE_COLLECTSTATIC | 1 |

14. Add the hostname of your Heroku app to allowed hosts in settings.py

15. Now you can commit all the changes and push to GitHub;

        $ git add . 
        $ git commit -m <'your commit message'>
        $ git push

16. If you created your app on the website you will need to initialize your     Heroku git remote using the following command;

        $ heroku git:remote -a fit-heatlhty-body

17. Then use the following command to push to Heroku;

        $ git push heroku master

## Media

All images used were downloded on google 

## Acknowledgements
My Mentor.

The help and support received from the tutors at Code Institute.

The Code Institute Slack Community.
