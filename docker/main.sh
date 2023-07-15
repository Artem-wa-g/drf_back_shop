#!/bin/bash

python manage.py makemigrations

python manage.py migrate

uvicorn app.asgi:application --host 0.0.0.0 --reload