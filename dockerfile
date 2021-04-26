FROM python:rc-alpine3.13

LABEL maintainer "j.melard@outlook.com"

RUN apk add --no-cache py3-pip

# We copy just the requirements.txt first to leverage Docker cache
COPY ./prod_requirements.txt /app/prod_requirements.txt

WORKDIR /app

RUN pip3 install -r prod_requirements.txt

COPY . /app

EXPOSE 5000

ENTRYPOINT [ "python3" ]

CMD [ "calculatrice.py" ]