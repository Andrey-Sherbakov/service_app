# 💳 Service app
**Django rest framework** приложение для работы с подписками. 

_Учебное приложение в котором я изучал способы оптимизации джанго такие как **Celery** для отложеных
задач, ручное кэширование с **Redis** и правильная инвалидация кэша, а также грамотную работу с **ORM**._

## ⚙️ Технологии
* **Django Rest Framework** - бэкенд фреймворк
* **PostgreSQL** - база данных
* **Celery** - инструмент для отложенных задач
* **Redis** - кэширование
* **Docker** - контейнеризация
* **Adminer** - работа с базой данных
* **Flower** - отслеживание отложенных задач

## 🚀 Установка и запуск
1. Клонировать репозиторий:
    ```shell
    git clone https://github.com/Andrey-Sherbakov/service_app.git
    cd service_app
    ```
2. Собрать и запустить :whale: Docker compose:
   ```shell
   docker compose build
   docker compose up
   ```
4. Применить миграции:
   ```shell
   docker compose exec web-app python manage.py migrate
   ```
4. Загрузить фикстуры в базу данных либо создать нового суперпользователя:
   * **Фикстуры**:
     ```shell
     docker compose exec web-app python manage.py loaddata db.json
     ```
     _Данные суперпользователя: логин - **root**, пароль - **1234**_
   * **Новый суперпользователь**:
     ```shell
     docker compose exec web-app python manage.py createsuperuser
     
     Username: # введите свой логин
     Email address: # введите свой email (опционально)
     Password: # введите пароль
     Password (again): # повторите пароль
     ```

## 🖥️ Сервисы:
После запуска docker compose будут доступны следующие сервисы:
* http://127.0.0.1:8000/admin/ - админ панель для администрирования
![image](https://drive.google.com/uc?id=1O3J5m9Bz9pKc0-o2Jv771Nv-Hm79jlrw)
* http://127.0.0.1:8080/ - adminer для работы с базой данных
    ```
    Данные для входа:
  
    Сервер - database
    Имя пользователя - dbuser
    Пароль - pass
    База данных - dbname
    ```
    ![image](https://drive.google.com/uc?id=1et7nmpD5RTj4BpGxs-Cy61BWHLtXAxIh)
* http://127.0.0.1:5555/ - Flower для отслеживания отложенных Celery задач
![image](https://drive.google.com/uc?id=1WbExFS4SVI6ayyBRtDFMgRfEJHEoF47f)

## 🌐 API
* http://127.0.0.1:8000/api/subscriptions/ - GET для получения всех подписок, POST для создания новой подписки
* http://127.0.0.1:8000/api/subscriptions/{id}/ - GET, PUT, DELETE для чтения, изменения и удаления подписки по **id**

## 📁 Структура проекта
```
.
├── service
│   ├── clients
│   │   ├── migrations
│   │   │   └── ...
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── models.py
│   │   ├── tests.py
│   │   └── views.py
│   ├── service
│   │   ├── asgi.py
│   │   ├── settings.py
│   │   ├── tasks.py
│   │   ├── urls.py
│   │   └── wsgi.py
│   ├── services
│   │   ├── migrations
│   │   │   └── ...
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── models.py
│   │   ├── serializers.py
│   │   ├── signals.py
│   │   ├── tests.py
│   │   └── views.py
│   ├── celery_app.py
│   ├── db.json
│   └── manage.py
├── Dockerfile
├── LICENSE
├── README.md
├── docker-compose.yml
└── requirements.txt
```