# Products

Склонировать репозиторий: `git clone https://github.com/viktornikolaev1995/image_compression

## Настройка проекта

Перейти в папку проекта: `cd core`

Создайте файл для переменных окружения .env через команду: `cp .example.env .env` и внесите при необходимости корректировки

Создайте виртуальное окружение: `poetry shell`

Установите зависимости: `poetry install`

Создайте по перменным окружения базу данных: `psql -U postgres` -> `create database POSTGRES_DB;`

Применение миграций: `poetry run python manage.py migrate`

Создание суперпользователя: `poetry run python manage.py createsuperuser`

Запуск приложения: `poetry run python manage.py runserver`
