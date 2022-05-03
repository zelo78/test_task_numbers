# Пустой проект на Django и DRF

Универсальный пустой шаблон для создания проектов с использованием **Django**, **Django REST framework**, **PostgreSQL**, **Docker**, **Docker-compose**.

### Запуск

1. Клонировать проект `git clone`.
2. Проверить наличие файла `.env` в корне проекта (рядом с `docker-compose.yml`).
3. Запустить контейнер:
```shell
docker-compose up -d
```
4. Создать суперпользователя:
```shell
docker exec -it app python manage.py createsuperuser
```

### Реализованные URL

- <http://0.0.0.0:8000/admin/> - интерфейс администрирования
- <http://0.0.0.0:8000/api/> - API интерфейс
- <http://0.0.0.0:8000/api/token/> - API авторизации

### Swagger/OpenAPI 2.0 specifications

- <http://0.0.0.0:8000/swagger/> - A swagger-ui view of your API specification 
- <http://0.0.0.0:8000/swagger.json> - A JSON view of your API specification 
- <http://0.0.0.0:8000/swagger.yaml> - A YAML view of your API specification
- <http://0.0.0.0:8000/redoc/> - A ReDoc view of your API specification 

### Авторизация

1. Получение токена
```shell
curl \
  -X POST \
  -H "Content-Type: application/json" \
  -d '{"username": "oleg", "password": "12345678"}' \
  http://127.0.0.1:8000/api/token/
```
2. Авторизация с использованием токена
```shell
curl \
  -H "Authorization: Bearer <token>" \
  http://127.0.0.1:8000/api/users/
```

## Использованные библиотеки

- [Django](https://www.djangoproject.com/) v. 4.0.4
- [Django REST framework](https://www.django-rest-framework.org/) v. 3.13.1
- [Psycopg](https://www.psycopg.org/docs/) v. 2.9.3 - PostgreSQL database adapter for Python
- [drf-yasg](https://drf-yasg.readthedocs.io/en/stable/) v. 1.20.0 - Yet another Swagger generator. Generate real Swagger/OpenAPI 2.0 specifications from a Django Rest Framework API
- [Simple JWT](https://django-rest-framework-simplejwt.readthedocs.io/en/latest/) v. 5.1.0 - Simple JWT provides a JSON Web Token authentication backend for the Django REST Framework
- [python-dotenv](https://pypi.org/project/python-dotenv/) v. 0.20.0 - Reads key-value pairs from a `.env` file and can set them as environment variables
- [black](https://black.readthedocs.io/en/stable/) v. 22.3.0 - The uncompromising code formatter
 