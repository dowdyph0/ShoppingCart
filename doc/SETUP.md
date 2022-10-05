The application needs the following secret files to be created under the folder "secrets".

    - db_name
    - db_password
    - db_user
    - django_secret_key
    - redis_password

If docker is running in swarm mode, the file section of each secret in docker-compose.yml must be removed