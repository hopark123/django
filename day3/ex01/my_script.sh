#!/bin/bash

PYTHON_PATH="/usr/bin/python3"
PATH_PY_URL="https://github.com/jaraco/path.git"
VEN_DIR="local_lib"
LOG_FILE="pip_install.log"

# setup venv
$PYTHON_PATH -m venv $VEN_DIR
source $VEN_DIR/bin/activate

# python version
python -m pip --version

# pip upgrade
pip install --upgrade pip

# path install
python -m pip install -q git+$PATH_PY_URL -I --log $LOG_FILE

# start progam
python3 my_program.py