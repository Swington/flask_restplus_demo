FROM tiangolo/uwsgi-nginx-flask:python3.7

WORKDIR /app

COPY . /app

RUN pip install pipenv
RUN pipenv install --system --deploy --ignore-pipfile

ENV STATIC_INDEX 1