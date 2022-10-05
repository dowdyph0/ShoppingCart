#!/bin/sh

gunicorn project.asgi -k uvicorn.workers.UvicornWorker --log-level=${LOGLEVEL} --log-file - --timeout 60 -b unix:${UNIX_SOCKET_DIR}/backend.sock