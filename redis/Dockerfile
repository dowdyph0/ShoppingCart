FROM redis:7
RUN apt-get update && apt-get -y install gettext-base
COPY ./entrypoint.sh /redis/
COPY ./redis.conf.template /redis/
WORKDIR /redis/
RUN chmod +x /redis/entrypoint.sh