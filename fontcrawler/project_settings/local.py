"""EXAMPLE local config"""
DEBUG = True

ALLOWED_HOSTS = ['*']

SECRET_KEY = "by1!q%kl*r%omxw3_ln*)(b6za+u90qf_&wxzv802khv*el#k!"

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'postgres',
        'USER': 'postgres',
        'PASSWORD': 'postgres',
        'HOST': 'db',
        'PORT': '5432',
    }
}

CELERY_BROKER_URL = 'amqp://rabbitmq:rabbitmq@rabbitmq:5672'
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_RESULT_BACKEND = 'django-db'

