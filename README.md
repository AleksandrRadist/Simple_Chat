## Simple Chat Rooms

Мини проект, который предоставляет комнаты, внутри которых можно общаться с помощь чата.

### Installing

Проект использует:
- django - https://www.djangoproject.com,
- celery - https://docs.celeryproject.org/en/stable/index.html,
- redis - https://redis.io,
- django channels - https://channels.readthedocs.io/en/stable/.

### Чтобы запустить проект необходимо:

Создать и активировать виртуальное окружение:

    'python -m venv venv'
    'venv\Scripts\activate'

Установить зависимости: 

    'pip install -r requirements.txt'
    
Запустить миграции: 

    'python manage.py migrate

Создаать суперпользователя:

    'python manage.py createsuperuser'
    
Запустить redis:

    'docker-compose up'
    
Запустить celery:

    'celery -A simple_chat beat'
    'celery -A simple_chat worker -l INFO --pool=solo'

Запустить сервер:
    
    'python manage.py runserver'
