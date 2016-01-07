Inventory project with Django
=============================

An inventory demo project with Python an Django 1.9 using twitter bootstrap 3 and pagination.

Installation
-----------------------------

- Install [Python](http://www.python.org/) (if you are using Linux, you already have Python installed)
- Install [Django](http://www.djangoproject.com)
- Install [Pip]() to manage dependencies

Database
-----------------------------

I have an SQLite database. To browse and manage data, you can use [sqlbrowser](http://sqlitebrowser.org/).

Run the server
-----------------------------

	python manage.py runserver

Now you can visit the application URL: http://localhost:8000/

Administration
-----------------------------

Now you can access the admin area:

	http://localhost:8000/admin/

Create a superuser:

	python manage.py createsuperuser

Testing
-----------------------------

To run all unit test:

	python manage.py test

TODO
-----------------------------

Some next steps about practicing web development with Python:

- Create a Categories table
- Switch to MySQL and use joins
- Admin area with many-to-many data relationships
- Admin area template customization
- Using Django REST framework

Deployment
-----------------------------

Here is a simple list about a Django application deployment:

- Be sure to upload the files on your server and have Django installed on your server
- Set debug mode to false: on settings.py simply change DEBUG = False

