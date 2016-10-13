FROM python:3.5-alpine

WORKDIR /var/www

RUN pip install tox pytest flake8 flake8-quotes

COPY ./lib /var/www/lib
