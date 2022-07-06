#!/bin/sh

export FLASK_APP=./opencourse/index.py

source $(pipenv --venv)/bin/activate

python $FLASK_APP