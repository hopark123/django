#!/bin/bash

PYTHON_PATH="/usr/bin/python3"
VEN_DIR="venv_rush01"

# setup venv
$PYTHON_PATH -m venv $VEN_DIR
source $VEN_DIR/bin/activate

# python version
python -m pip --version

# pip upgrade
pip install --upgrade pip

# pip install 
python -m pip install -q -I django psycopg2-binary pillow gunicorn bash


# nginx install
# brew install nginx


# make requirement.txt
pip freeze > requirement.txt

# sever start
# django-admin startproject boot
# python3 manage.py startapp ex00
python3 ./rush01/manage.py makemigrations
python3 ./rush01/manage.py migrate
python3 ./rush01/manage.py runserver --insecure


# brew services start nginx

#error
# pip install --upgrade --force-reinstall Django

# migrations del
# find . -path "*/migrations/*.py" -not -name "__init__.py" -delete
# find . -path "*/migrations/*.pyc"  -delete

# docker-compose build

# docker build --no-cache --network=host -t durumi .
# docker run -p 8000:8000 77cdf4a93ef5