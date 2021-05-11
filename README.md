## Fit Healthy Body 

It is a website that sell fitness equipment, nutrients plans to make your body heatlhty and be physically fit, exercise plans were you will follow a well devised plan on what type of exercise you have to do to target different parts of the body

#### For testing the following credentials can be used:

##### Member Login

Username: tinashe

Email: tinashechasakara@gmail.com

Password: Deca5959

Card payments

Card number: 4242 4242 4242 4242

Zip & CCV: any integer values are valid

### User profiles

#### Site Visitor 
As a site visitor, I want to be able to easily navigate around the site and gain a clear insight into its purpose. I would like to be able to browse the services and products on offer with the option to purchase and the option to register as a member for more resources.

#### Site Member
 As a site member, I want to be part of a community where I can interact with other members around key topics to share each other's knowledge, experience, and progress. I would like to have my own user profile to store my personal details and order history, and the ability to easily log in and out of the site.

#### Site Owner
 As the site owner, I want to be able to continually monitor and update the site to manage my user's expectations. I would like the ability to easily add, edit and delete products to ensure my site is always up to date and relevant. I want to provide a customer review option, to gain feedback for improvements, and to develop a sense of transparency to gain consumer loyalty and trust.

### Wireframes 

## Features used

Responsive on all device sizes

Mobile-first design, responsive on all devices through using the Bootstrap grid system and CSS media queries.
A user-friendly interface with easy navigation throughout the site

Attractive, minimalistic design with visuals and information presented clearly and concisely.

Easily readable fonts and simple navigation throughout the site.

Fixed navigation bar visible on every page featuring a dropdown menu, easily recognisable icons and brand logo to link back to the homepage.
Search bar accessible from every page allowing the user to easily search the site by keywords.
Clear interactive buttons used for an effortless user journey throughout the site.
Toasts used throughout the site to display alert messages to the user to assist on their journey.
Home

Home

#### Products
sort and filter functionality to allow users to easily find products they are looking for.
Card listings have been used to display product image, name, price and rating.

####  Product Detail
crispy forms used for elegant formatting.
Size selector option for sized products to allow user to select a size.
Quantity selector option to allow user to select a quantity.
add to bag button to allow user to add the product to bag.

#### Product Admin
Forms have been used to allow the admin user to add and edit products manually on the site.

#### Bag
A fully functioning shopping bag allowing users to add both products and programmes they wish to buy
Quantity selector with option to update or remove item from bag
Clear Secure Checkout button to take user to checkout
An arrow displayed at the bottom of the bag to easily direct the user back to the navigation options

#### Checkout
A order summary displaying all the items the user has in their bag ready to purchase.
crispy forms used for elegant formatting.
Forms used to display personal, delivery and payment fields.
Option for user to click 'Save this delivery information to my profile' to save details to their profile page.
Stripe payments used to manage site card transactions.

#### Checkout Success
The checkout success page provides reassurance for the user that their purchase has gone through and displays all their order details.
Order confirmation sent to the user's personal email after they complete checkout.

#### Blog
A Blog was added so that users who have used our products can testify how they have changed their heatlhty be it mentally or physically. Users can also share how best to use the product.

#### Profile
crispy forms used for elegant formatting.
Forms used to display users personal details.
Option for user to click 'update details' to save details to profile.
A table has been used to display the user's order history including order number, order date and order total. There is also a button 'view order details' which links to the checkout success page showing the specific order details.

#### Authorisation
All authorisation pages including register, login and logout have been implemented through Django allauth account. CSS styling has been applied to ensure pages match the sites overall design spec.

Social login has been implemented through Django allauth socialaccount giving the user the option to login through Google, Facebook or Twitter.

[Wireframes](https://c14b6c1d-0386-44b5-9bef-ce64ddf62c2b.ws-eu03.gitpod.io/files/download/?id=1b302be3-2173-4eb5-9c35-2a3f7d52b49b)

## Technnologies used

### Languages used

##### HTML5
##### CSS3
##### JavaScript
#####  Python

#### Frameworks, Libraries & Programs

[Django](https://www.djangoproject.com/)

* Python web framework used to build the site.

[Git](https://git-scm.com/)

* Git was used for version control by utilizing the Gitpod terminal to commit to Git and push to GitHub.

[GitHub](https://github.com/)

* GitHub is used to store the project code after being pushed from Git.

[Heroku](https://id.heroku.com/)

* Heroku is the app platform I deployed my project to.
Heroku Postgres.Heroku’s reliable and powerful database used to store the data for my deployed Heroku App.

[jQuery](https://jquery.com/)

* A javascript library used to simplify DOM manipulation.

[Bootstrap 4.5.3](https://getbootstrap.com/)

* Bootstrap was used to assist with the responsiveness and styling of the website using design templates.

[Boto3](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html)

* Python SDK for AWS, used to directly create, update, and delete AWS resources from my Python scripts.

[gunicorn](https://gunicorn.org/)

* WSGI server used to take care of everything happening between the web server and web application.

[Pillow](https://pypi.org/project/Pillow/2.2.1/)

* Python Imaging Library (PIL), used to add support for opening, manipulating, and saving images.

[psycopg2](https://pypi.org/project/psycopg2/)

* PostgreSQL database adapter

[AWS](https://aws.amazon.com/)

* A cloud-based storage service used to store static and, media files.

[Stripe](https://stripe.com/gb)

* Stripe was used to deal with payments.

[Temp Mail](https://temp-mail.org/en/)

* Temp Mail was used to provide temporary, secure, anonymous, free, disposable email addresses for testing purposes.

[Google fonts](https://fonts.google.com/)

Google fonts were used to import the fonts into the CSS file which is used on all pages throughout the project.

[Font Awesome 4.7.0](https://fontawesome.com/)

* Font Awesome was used to add icons for aesthetic and UX purposes.

[HTML Formatter](https://www.freeformatter.com/html-formatter.html) and [CSS Formatter](https://www.freeformatter.com/css-beautifier.html)

* Used to format my HTML and CSS files with the desired indentation level for optimal readability.

[Techsini](http://techsini.com/multi-mockup/index.php)

* Multi Device Website Mockup Generator Tool

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
