#!/bin/bash

sleep 25000

python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py runserver 0.0.0.0:80