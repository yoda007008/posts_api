# Посты 

## Описание

Этот проект представляет собой веб-приложение, разработанное на фреимворке FastAPI. Оно предоставляет API для выполнения различных операций с данными, хранящимися в базе данных PostgreSQL. Проект использует SQLAlchemy для работы с базой данных и Pytest для тестирования.

## Использованные технологии

- **FastAPI**: Современный веб-фреймворк для создания API на Python. Быстрый и простой в использовании, с поддержкой асинхронного программирования.
  
- **PostgreSQL**: Реляционная база данных, которая обеспечивает надежное и мощное хранилище для данных приложения.
  
- **SQLAlchemy**: ORM (Object-Relational Mapping) библиотека для Python, которая упрощает работу с базами данных, позволяя разработчикам использовать Python-объекты вместо SQL-запросов.
  
- **Pytest**: Фреймворк для тестирования в Python, который позволяет писать простые и масштабируемые тесты для вашего приложения.

## Установка и запуск

Для запуска приложения в контейнере Docker, выполните следующие команды:

1. Склонируйте репозиторий:

   ```bash
   git clone https://github.com/yoda007008/posts_api.git
   ```
2. Примените миграции:

   ```bash
   alembic upgrade head
   ```
3. Сборка Docker образа:

   ```bash
   docker-compose build .
   ```

4. Запустите контейнер:

   ```bash
   docker-compose up
   ```

Теперь приложение будет доступно по адресу `http://localhost:9000`.



