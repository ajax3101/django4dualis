# Приклад Веб-сайту на Django4 присвячений "Дуальной освіті" 
[![Python Version](https://img.shields.io/badge/python-3.10-brightgreen.svg)](https://python.org)
[![Django Version](https://img.shields.io/badge/django-4.0-brightgreen.svg)](https://djangoproject.com)

Пишемо веб-сайт на фреймворку Django4, Bootstrap, присвячений "Дуальной освіті".

## Running the Project Locally

First, clone the repository to your local machine:
```bash
$ git clone https://github.com/ajax3101/django4dualis.git
$ cd django4dualis/
```
Install the requirements:
```bash
$ python -m venv venv 
$ pip install -r requirements.txt
$ cd dualis/
$ python manage.py migrate
$ python manage.py createsuperuser
$ python manage.py runserver
```