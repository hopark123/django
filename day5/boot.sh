#!/bin/bash

PYTHON_PATH="/usr/bin/python3"
VEN_DIR="day05_venv"

# setup venv
$PYTHON_PATH -m venv $VEN_DIR
source $VEN_DIR/bin/activate

# python version
python -m pip --version

# pip upgrade
pip install --upgrade pip

# pip install 
python -m pip install -q -I django psycopg2-binary psycopg2-binary

brew install PostgreSQL
# make requirement.txt
pip freeze > requirement.txt

# sever start
# django-admin startproject d05
# cd d05
# python3 manage.py startapp ex00
# python3 manage.py runserver
# python3 manage.py makemigrations
# python3 manage.py migrate


#error
# pip install --upgrade --force-reinstall Django


# migrations del
# find . -path "*/migrations/*.py" -not -name "__init__.py" -delete
# find . -path "*/migrations/*.pyc"  -delete

