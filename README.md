# Шаблон проекта на Django и Django REST framework

Универсальный пустой шаблон для создания проектов с использованием **Django**, **Django REST framework**, **PostgreSQL**, **Docker**, **Docker-compose**.

## Установка

1. Клонировать проект в пустую папку:
```shell
git clone https://github.com/zelo78/DRF-project-template.git .
```

2. Копировать файл `start.env` как `.env` (Он должен находится в корне проекта, рядом с `README.md`)
```shell
cp start.env .env
```

3. Создать и запустить контейнер (при запуске контейнера будут созданы и применены миграции):
```shell
docker-compose up -d --build
``` 

4. Создать суперпользователя:
```shell
docker exec -it zapp python manage.py createsuperuser --username USER
```

5. Остановить контейнер
```shell
docker-compose down
```

## Запуск
```shell
docker-compose up
``` 

## Реализованные URL

- <http://0.0.0.0:8000/admin/> - интерфейс администрирования
- <http://0.0.0.0:8000/api/> - API интерфейс
- <http://0.0.0.0:8000/api/token/> - API авторизации

### Swagger/OpenAPI 2.0 specifications

- <http://0.0.0.0:8000/swagger/> - A swagger-ui view of your API specification 
- <http://0.0.0.0:8000/swagger.json> - A JSON view of your API specification 
- <http://0.0.0.0:8000/swagger.yaml> - A YAML view of your API specification
- <http://0.0.0.0:8000/redoc/> - A ReDoc view of your API specification 

### Авторизация

#### Авторизация с помощью *BasicAuthentication* 
```shell
curl \
  -X GET \
  -H "Content-Type: application/json" \
  -u USER:PASSWORD \
  http://0.0.0.0:8000/api/users/
```

#### Авторизация с помощью *JWT*

- создаём токен авторизации
```shell
curl \
  -X POST \
  -H "Content-Type: application/json" \
  -d '{"username": "USER", "password": "PASSWORD"}' \
  http://0.0.0.0:8000/api/token/
```

Получаем ответ вида
> {"refresh":"ey...I0","access":"ey...lQ"}

- авторизуемся с помощью токена:
```shell
curl \
  -X GET \
  -H "Authorization: Bearer ey...lQ" \
  http://0.0.0.0:8000/api/users/
```

## Использованные библиотеки

- [Django](https://www.djangoproject.com/) v. 4.0.4
- [Django REST framework](https://www.django-rest-framework.org/) v. 3.13.1
- [Psycopg](https://www.psycopg.org/docs/) v. 2.9.3 - PostgreSQL database adapter for Python
- [drf-yasg](https://drf-yasg.readthedocs.io/en/stable/) v. 1.20.0 - Yet another Swagger generator. Generate real Swagger/OpenAPI 2.0 specifications from a Django Rest Framework API
- [Simple JWT](https://django-rest-framework-simplejwt.readthedocs.io/en/latest/) v. 5.1.0 - Simple JWT provides a JSON Web Token authentication backend for the Django REST Framework
- [python-dotenv](https://pypi.org/project/python-dotenv/) v. 0.20.0 - Reads key-value pairs from a `.env` file and can set them as environment variables
- [black](https://black.readthedocs.io/en/stable/) v. 22.3.0 - The uncompromising code formatter
 