FROM node:16 AS frontend_build
RUN yarn global add @quasar/cli
COPY . /frontend
WORKDIR /frontend
RUN yarn  --silent
RUN quasar build --mode spa --quiet


FROM nginx:1.23.1
COPY --from=frontend_build /frontend/dist/spa/ /usr/share/nginx/html