FROM python:3.9-alpine

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

RUN apk update \
    && apk add --virtual build-deps gcc python3-dev musl-dev \
    && apk add postgresql-dev \
    && apk add zlib-dev jpeg-dev \
    && apk add build-base \
    && pip install --upgrade pip

COPY . /app/

RUN pip install -r requirements.txt

RUN python manage.py migrate

CMD celery -A fampay_youtube_api worker -l INFO -E &

CMD celery -A fampay_youtube_api beat -l INFO &

CMD python manage.py runserver 0.0.0.0:8000

# docker build -t fampay_youtube_api .
# docker run -p 8000:8000 -e DJANGO_SETTINGS_MODULE=fampay_youtube_api.settings -e CELERY_BROKER_URL=redis://redis:6379/0 -e CELERY_RESULT_BACKEND=redis://redis:6379/0 fampay_youtube_api

