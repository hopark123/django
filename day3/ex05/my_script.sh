#!/bin/bash

PYTHON_PATH="/usr/bin/python3"
VEN_DIR="django_venv"

# setup venv
$PYTHON_PATH -m venv $VEN_DIR
source $VEN_DIR/bin/activate

# python version
python -m pip --version

# pip upgrade
pip install --upgrade pip

# pip install 
python -m pip install -q -I django psycopg2-binary

# make requirement.txt
pip freeze > requirement.txt

###########server 
# DJANGO_DIR="mysite"

# django-admin startproject $DJANGO_DIR
# python3 ./$DJANGO_DIR/manage.py runserver
# python3 ./$DJANGO_DIR/manage.py startapp 

# http://127.0.0.1:8000/hello/