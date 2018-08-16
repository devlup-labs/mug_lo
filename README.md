# MugLo ![Status active](https://img.shields.io/badge/Status-active%20development-2eb3c1.svg) ![Django 2.1](https://img.shields.io/badge/Django-2.1-green.svg) ![Python 3.6](https://img.shields.io/badge/Python-3.6-blue.svg)
[![Build Status](https://travis-ci.org/devlup-labs/mug_lo.svg?branch=master)](https://travis-ci.org/devlup-labs/mug_lo)
## A platform for sharing notes within a group of users

### Installation:
Requirements:
- Python 3.6 runtime
- Django 2.1
- Other dependencies in `Pipfile`

> For Vuetify UI build steps, follow [this](ui/README.md)

Procedure:
- Install [python](https://www.python.org/downloads/) in your environment(pre-installed on Ubuntu).
- Navigate to the cloned repository.
    ```
    cd <project_directory_name>     # mug_lo
    ```
- Install `pipenv` for dependency management
    ```
    pip install pipenv
    ```
- Use pipenv to install other dependencies from `Pipfile`
    ```
    pipenv install --dev
    ```
- Change to `src` directory and optionally activate virtual environment, if you don't want to activate env, use `pipenv run` to run python scripts
    ```
    cd src
    source "$(pipenv --venv)"/bin/activate
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
