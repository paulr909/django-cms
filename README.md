[![Python Version](https://img.shields.io/badge/python-3.9-brightgreen.svg)](https://python.org)
[![Django Version](https://img.shields.io/badge/django-4.0.1-brightgreen.svg)](https://djangoproject.com)

# Django CMS, Online Courses

## Django 4.0.1

Run your app in a Virtual Environment: [http://python-guide-ru.readthedocs.io/en/latest/dev/virtualenvs.html](http://python-guide-ru.readthedocs.io/en/latest/dev/virtualenvs.html)

Install the requirements:
```bash
pip install -r requirements.txt
```

Run the development server:
```bash
python manage.py runserver
```

Run Memcached:
```bash
memcached -l 127.0.0.1:11211
```

Site available at **127.0.0.1:8000/**

For Instructors login and course creation use this URL:
[http://127.0.0.1:8000/accounts/login/?next=/course/mine/](http://127.0.0.1:8000/accounts/login/?next=/course/mine/)