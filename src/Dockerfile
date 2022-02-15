FROM python:3.9
#FROM python:3.9-slim

#MAINTAINER Alex Mattson "alex.mattson@gmail.com"

COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip install -r requirements.txt

COPY . /app

RUN addgroup --system appuser && adduser --system appuser --ingroup appuser
USER appuser

ENTRYPOINT [ "python" ]

CMD [ "server.py" ]