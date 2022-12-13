# celery_project

## Описание
Развертывание Celery с Redis (+ Django и Postgres) в Docker  

## Стек технологий
- Python 3.8.10
- Django 4.1.4
- Celery 5.2.7
- Redis 4.4.0
- Docker-compose 3.8
- Postgres 12.4
- Nginx 1.19.3
- Gunicorn 20.1.0

## Установка docker
https://docs.docker.com/engine/install/

## Команды
### Клонирование репозитория
```bash
git clone https://github.com/docker581/celery_project
```

### Пример файла .env
```bash
DJANGO_SECRET_KEY=[django secret key]
DB_ENGINE=django.db.backends.postgresql 
DB_NAME=postgres 
POSTGRES_USER=postgres 
POSTGRES_PASSWORD=postgres
DB_HOST=db 
DB_PORT=5432
CELERY_BROKER=redis://redis:6379/0
DEBUG=True
```

### Запуск приложения
```bash
docker-compose up -d
```

### Создание суперпользователя
```bash
docker-compose exec django python manage.py migrate --noinput
docker-compose exec django python manage.py createsuperuser
```

## Автор
Докторов Денис
