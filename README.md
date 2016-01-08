Inventory project with Django
=============================

An inventory demo project with Python an Django 1.9 using twitter bootstrap 3 and pagination.

Installation
-----------------------------

- Install [Python](http://www.python.org/) (if you are using Linux, you already have Python installed)
- Install [Django](http://www.djangoproject.com)
- Install [Pip](https://pip.pypa.io/en/stable/installing/) to manage dependencies

Install these features using Pip;

- [Bootstrap Form App](https://github.com/tzangms/django-bootstrap-form)
- [Minify HTML](https://github.com/cobrateam/django-htmlmin)
- [Django REST framework](http://www.django-rest-framework.org/)

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

REST APIs
-----------------------------

Here are the REST calls (made with Django REST framework)

- Items list: GET /api/v1/items/
- Item details: GET /api/v1/items/{id}
- Delete an item: DELETE /api/v1/items/{id}
- Insert a new item; POST /api/v1/items/

Deployment
-----------------------------

Django deployment chelist:

- Be sure to upload the files on your server and have Django installed on your server
- Set debug mode to false: on settings.py simply change DEBUG = False
- Check every kind of tests (unit tests and functional tests etc.)

TODO
-----------------------------

Some next steps about practicing web development with Python and Django:

- Switch to MySQL and use joins (with a category table for example)
- Admin area with many-to-many data relationships
- Admin area template customization
- Database tree structure with parent child relationship