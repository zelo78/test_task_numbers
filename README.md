# Тестовое задание *Social network* (simple REST API)

Решение тестового задания компании [Webtronics](https://webtronics.ru/) с использованием **Django**, **Django REST framework**, **PostgreSQL**, **Docker**, **Docker-compose**.

Само задание приведено ниже.

## Установка

1. Клонировать проект в пустую папку:
```shell
git clone https://github.com/zelo78/test_task_webtronics.git .
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

5. В целях тестирования, базу данных можно наполнить данными (пользователи и их посты)
```shell
docker exec -it zapp python manage.py populatebase
```

7. Остановить контейнер
```shell
docker-compose down
```

## Запуск
```shell
docker-compose up
``` 

## Реализованные интерфейсы

### Командная строка

- [x] `python manage.py manage.py populatebase <count: int>`

  - Наполнение базы данных случайными Сообщениями в целях тестирования, общее число Сообщений будет не меньше `count`

### Реализованные API

- [ ] `POST /api/post/create/`
  - создание Сообщения
  - только авторизованными пользователями
  
- [ ] `GET /api/post/`
  - получение списка Сообщений

- [ ] `GET /api/post/<id: int>/`
  - получение конкретного Сообщения
  - автор сообщения видит больше информации, чем остальные

- [ ] `PATCH /api/post/<id: int>/`
  - частичное обновление Сообщения
  - доступно только его автору

- [ ] `DELETE /api/post/<id: int>/`
  - удаление Сообщения
  - доступно только его автору

- [ ] `POST /api/post/<id: int>/like/`
  - пометить Сообщение как "понравившееся" (like)
  - только от авторизованного пользователя
  - автор метки сохраняется в БД и эта информация доступна автору Сообщения
  - метки "понравилось" и "не понравилось" являются взаимоисключающими, установка одной удаляет другую

- [ ] `POST /api/post/<id: int>/unlike/`
  - пометить Сообщение как "непонравившееся" (unlike)
  - только от авторизованного пользователя
  - автор метки сохраняется в БД и эта информация доступна автору Сообщения
  - метки "понравилось" и "не понравилось" являются взаимоисключающими, установка одной удаляет другую

- [x] `POST /api/token/`
  - получение токена JWT авторизации

- [ ] `POST /api/users/`
  - создание нового Пользователя

- [ ] `GET /api/users/`
  - получение списка Пользователей
  - только для Администраторов

- [ ] `GET /api/users/<id: int>/`
  - получение информации по конкретному пользователю
  - только для Администраторов или о самом себе

- [ ] `PATCH /api/users/<id: int>/`
  - частичное обновление Пользователя
  - только для Администраторов или о самого себя

- [ ] `DELETE /api/users/<id: int>/`
  - удаление Пользователя
  - только для Администраторов

### Реализованные URL

- [x] <http://0.0.0.0:8000/admin/>
  - интерфейс администрирования

### Swagger/OpenAPI 2.0 specifications

- [ ] <http://0.0.0.0:8000/swagger/> 
  - A swagger-ui view of your API specification 
- [ ] <http://0.0.0.0:8000/swagger.json> 
  - A JSON view of your API specification 
- [ ] <http://0.0.0.0:8000/swagger.yaml> 
  - A YAML view of your API specification
- [ ] <http://0.0.0.0:8000/redoc/> 
  - A ReDoc view of your API specification 

### Авторизация

#### Авторизация с помощью *BasicAuthentication* 
```shell
curl \
  -X GET \
  -H "Content-Type: application/json" \
  -u USER:PASSWORD \
  http://0.0.0.0:8000/api/post/
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

- получаем ответ вида
> {"refresh":"ey...I0","access":"ey...lQ"}

- авторизуемся с помощью токена:
```shell
curl \
  -X GET \
  -H "Authorization: Bearer ey...lQ" \
  http://0.0.0.0:8000/api/post/
```

## Примеры запросов 

## Тестовое задание **Социальная сеть**

Тестовое задание компании [Webtronics](https://webtronics.ru/).

Целью этого задания является создания простого REST API. Вы должны использовать Django и Django REST framework.

### Базовые модели

- Пользователь
- Сообщение (всегда создаётся Пользователем)

### Базовые возможности

- регистрация Пользователя
- авторизация Пользователя
- создания Сообщения
- пометить Сообщение как "понравившееся" (like)
- пометить Сообщение как "непонравившееся" (unlike)

Для Пользователей и Постов кандидаты могут определять аттрибуты наиболее подходящим на их взгляд образом.

### Требования

- аутентификация по токену (JWT предпочтителен)
- использование Django с дополнительными модулями, базами данных и т.п.

### Опционально (что будет плюсом)

- использование <https://clearbit.com/platform/enrichment> для получения дополнительной информации о Пользователях
- использование <https://hunter.io/> для подтверждения существования адреса электронной почты при регистрации 

### Время на реализацию

1 рабочий день

### Дополнительные требования

Результат должен быть выложен на [GitHub](https://github.com/), с документацией по тому, как можно развернуть проект и протестировать его.

## Использованные библиотеки

- [Django](https://www.djangoproject.com/) v. 4.0.4
- [Django REST framework](https://www.django-rest-framework.org/) v. 3.13.1
- [Psycopg](https://www.psycopg.org/docs/) v. 2.9.3 - PostgreSQL database adapter for Python
- [drf-yasg](https://drf-yasg.readthedocs.io/en/stable/) v. 1.20.0 - Yet another Swagger generator. Generate real Swagger/OpenAPI 2.0 specifications from a Django Rest Framework API
- [Simple JWT](https://django-rest-framework-simplejwt.readthedocs.io/en/latest/) v. 5.1.0 - Simple JWT provides a JSON Web Token authentication backend for the Django REST Framework
- [python-dotenv](https://pypi.org/project/python-dotenv/) v. 0.20.0 - Reads key-value pairs from a `.env` file and can set them as environment variables
- [black](https://black.readthedocs.io/en/stable/) v. 22.3.0 - The uncompromising code formatter
- [factory_boy](https://factoryboy.readthedocs.io/en/stable/) v 3.2.1 - Fixtures replacement tool, it aims to replace static, hard to maintain fixtures with easy-to-use factories for complex objects.
