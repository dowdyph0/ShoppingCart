FROM python:3.10
COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt
COPY . /backend
RUN chmod +x /backend/entrypoint.sh
WORKDIR /backend