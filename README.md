# MugLo ![Status active](https://img.shields.io/badge/Status-active%20development-2eb3c1.svg) ![Django 2.0.5](https://img.shields.io/badge/Django-2.0.5-green.svg) ![Python 3.6](https://img.shields.io/badge/Python-3.6-blue.svg)
[![Build Status](https://travis-ci.org/devlup-labs/mug_lo.svg?branch=master)](https://travis-ci.org/devlup-labs/mug_lo)
## A platform for sharing notes within a group of users
### Purpose
[GOES HERE]

### Installation:
Requirements:
- Python 3.6 runtime
- Django 2.0.5
- Other dependencies in `requirements.txt`

> For Vuetify UI build steps, follow [this](ui/README.md)

Procedure:
- Install [python](https://www.python.org/downloads/) in your environment(pre-installed on Ubuntu).
- Navigate to the cloned repository.
    ```
    cd <project_directory_name>     # mug_lo
    ```
- Create a new virtual environment and activate it.
    ```
    sudo apt-get install -y python3-venv
    python3 -m venv muglo_venv
    source muglo_venv/bin/activate
    ```
- Use pip to install other dependencies from `requirements.txt`
    ```
    pip install -r requirements.txt
    ```
- Change to `src` directory
    ```
    cd src
    ```
- Make database migrations
    ```
    python manage.py makemigrations --settings=mug_lo.settings
    python manage.py migrate --settings=mug_lo.settings
    ```
- Create a superuser
    ```
    python manage.py createsuperuser --settings=mug_lo.settings
    ```
- Run development server on localhost
    ```
    python manage.py runserver --settings=mug_lo.settings
    ```
