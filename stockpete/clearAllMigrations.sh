#!/bin/bash

# Script to delete all migrations and db,
# and start from scratch

# Use in case of monumental screw ups,
# when unable to fix

find . -path "*/migrations/*.py" -not -name "__init__.py" -delete
find . -path "*/migrations/*.pyc"  -delete
rm "db.sqlite3"
python ./manage.py makemigrations
python ./manage.py migrate

