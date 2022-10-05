#!/bin/sh

export REDIS_PASSWORD=$(cat /run/secrets/redis_password)
envsubst < redis.conf.template > /etc/redis.conf
redis-server /etc/redis.conf