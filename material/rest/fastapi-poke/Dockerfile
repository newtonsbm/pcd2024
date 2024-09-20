FROM python:3.7-alpine

WORKDIR /app

COPY . /app

EXPOSE 8000

RUN pip install -r requirements.txt

CMD uvicorn main:app --host 0.0.0.0 --reload
# python manage.py runserver 0.0.0.0:8000 
 