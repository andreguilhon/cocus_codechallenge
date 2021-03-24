#!/usr/bin/env bash
if [ -n "$DJANGO_SUPERUSER_USERNAME" ] && [ -n "$DJANGO_SUPERUSER_PASSWORD" ] ; then
    (cd filereader; python manage.py createsuperuser --no-input)
fi
python filereader/manage.py makemigrations
python filereader/manage.py migrate
(cd filereader; gunicorn filereader.wsgi --user www-data --bind 0.0.0.0:8010 --workers 3) &
nginx -g "daemon off;"