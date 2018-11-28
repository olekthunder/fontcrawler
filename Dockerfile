FROM python:3.4.9-slim

WORKDIR /app

COPY . /app

RUN pip install -r requirements.txt

expose 8000

CMD ["python", "manage.py", "runserver"]

