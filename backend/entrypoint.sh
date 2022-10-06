#!/bin/sh

python manage.py collectstatic --noinput
python manage.py migrate --noinput
python manage.py create_initial_superuser

gunicorn project.asgi -k uvicorn.workers.UvicornWorker --log-level=${LOGLEVEL} --log-file - --timeout 60 -b unix:${UNIX_SOCKET_DIR}/backend.sock