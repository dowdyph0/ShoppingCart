# Running the application

## Application requirements

- docker (https://www.docker.com/)
- docker-compose (https://docs.docker.com/compose/install/)


The application needs the following secret files to be created under the folder "secrets".

    - db_name
    - db_password
    - db_user
    - django_secret_key
    - redis_password

If docker is running in swarm mode, the file section of each secret in docker-compose.yml must be removed and define secrets using "docker secret create"

All the commands mentioned in this section must be run on the application base directory (the directory that contains the **docker-compose.yml** file)

## Start the application
```
docker-compose up -d
```

## Stop the application
```
docker-compose stop
```

## Stop and clean the volumes of the application
```
docker-compose down -v
```

## Check the application logs
```
docker-compose logs -f
```

## List application volumes
```
docker volume ls
```

> During the application running, the following volumes will be created, its important to realize that in **qvanteltest_db_data** and in **qvannteltest_media** volumes important application data are stored.

```
DRIVER              VOLUME NAME
....                ....
local               qvanteltest_backend_unix_socket
local               qvanteltest_db_data
local               qvanteltest_media
local               qvanteltest_static
local               qvanteltest_unix_socket_dir
```

## Ports
> The application will expose port 80 via HTTP Protocol on the host machine


## Default user
> The application runs by default by the following credentials
```
username: admin
password: admin1234
```

> Theese credentials can be overriden by defining the next environment variables on the backend service in the **docker-compose.yml** file
- DJANGO_DEFAULT_ADMIN_USERNAME
- DJANGO_DEFAULT_ADMIN_PASSWORD


## Environment variables
> The following environment variables can be customized

- ALLOWED_HOSTS *Comma separated list of hosts allowed to access the backend service*
- STATIC_ROOT *Path inside the backend container that contains static files*
- MEDIA_ROOT *Path inside the backend container that contains the media files (user uploads)*
- UNIX_SOCKET_DIR *Path to a folder for the unix socket that communicates the backend and the frontend*
- BACKEND_SOCKET *Path to a unix socket used for communicating the backend and the frontend*
- PYTHONDONTWRITEBYTECODE *Dont create .pyc files*
- PYTHONUNBUFFERED *Force the stdout and stderr streams to be unbuffered*
- LOGLEVEL *Log level of the UvicornWorker*
- NGINX_INTERNAL_PORT *Internal tcp port of the Nginx server*
- NGINX_EXTERNAL_PORT *External tcp port of the Nginx server*
- DB_ENGINE *Database engine used by django (refer to https://docs.djangoproject.com/en/4.1/ref/databases for changes)*

# Tuning

## Redis overcommit_memory (Background save may fail under low memory condition) edit /etc/sysctl.conf on host
vm.overcommit_memory=1


# Api

> All api description is found in the file **openapi.yaml** for complete browsing use (swagger.io) to browse

# NOTES
> This is just a demo, dont use it for a project base or production environment.