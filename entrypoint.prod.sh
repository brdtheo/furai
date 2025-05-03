#!/usr/bin/env bash

npm i theme/static_src # Install node modules for tailwind build
python manage.py tailwind install --no-package-lock --no-input;
python manage.py tailwind build
python manage.py collectstatic --noinput
python manage.py migrate --noinput
python -m gunicorn --bind 0.0.0.0:8004 --workers 3 furai.wsgi:application