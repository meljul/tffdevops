FROM python:rc-alpine3.13

LABEL maintainer "j.melard@outlook.com"

RUN apk add --no-cache py3-pip

# We copy just the requirements.txt first to leverage Docker cache
COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip3 install -r requirements.txt

COPY . /app

ENTRYPOINT [ "python3" ]

CMD [ "calculatrice.py" ]