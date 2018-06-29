# Web Database Management 
<p align="center">
    
    <img src="https://img.shields.io/badge/License-MIT-blue.svg" />
    <img src="https://img.shields.io/badge/Made%20with-Python-yellow.svg" />
    <img src=https://img.shields.io/badge/Made%20with-Django-green.svg />
    <img src=https://img.shields.io/badge/Database-mySQL-blue.svg />
    <a href="https://snyk.io/test/github/ajay340/Web-Database-Management?targetFile=requirements.txt"><img src="https://snyk.io/test/github/ajay340/Web-Database-Management/badge.svg?targetFile=requirements.txt" alt="Known Vulnerabilities" data-canonical-src="https://snyk.io/test/github/ajay340/Web-Database-Management?targetFile=requirements.txt" style="max-width:100%;"></a>
    <img src="/screenshots/screenshot1.png" />
</p>

This is a web application for viewing, adding, deleting, and editing data on your mySQL database created with Django.

## Documentation

* [Install](#how-to-install)
* [Running](#running)
* [Configuration](#configuration)
* [Screenshots](#screenshots)

## How to install
You will need to have Python 3.X and mySQL 5.7.X installed. 
mySQL verison 5.8+ is not compatible with some of the libraries.

Next install the required libraries.
```
pip3 install -r requirements.txt
```

## Running 
```
python3 manage.py runserver 0.0.0.0:8000
```

Then enter your web browser and go to [http://localhost:8000](http://127.0.0.1:8000)

## Configuration
You must create a schema in your mySQL server and it must allow your IP to have access to connect, read, and write.

First go to databasereach/settings.py and change the server specifications to your mySQL server setup.
```python
DATABASES = {
'default': {
    'ENGINE': 'django.db.backends.mysql',
    'NAME': '<schema>',
    'HOST': '',
    'PORT': '',
    'USER': '',
    'PASSWORD': '',
}}
```
Next go to materialdb/views.py and change the mySQL server specification.
```python
conn = pymysql.connect(host="", port=, user="", password="", db="<schema>")
```
Now in materialdb/models.py, change the model class with the name of your schema. Also you can change the names, add, or delete the columns. 
### If you do decide to alter the columns, you will need to change specifications in materialdb/adduser.html, materialdb/tables.html, materialdb/edituser.html, materialdb/views.py, and materialdb/forms.py
```python
class <schema>(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    country = models.CharField(max_length=30)
    city = models.CharField(max_length=40)
    salary = models.CharField(max_length=10)
```
Then migrate the columns to your schema using these commands.
```
python3 manage.py makemigrations
python3 manage.py migrate
```

And finally just run the server.

## Screenshots
Adding entries to the database
<p align="center"><img src="/screenshots/screenshot2.png"></p>
Editing entries in database
<p alight="center"><img src="/screenshots/screenshot3.png"></p>
