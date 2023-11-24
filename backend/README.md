# Urbaton

## Работа с приложением

### Требования

- `Docker` и `docker-compose`
- `Python 3.11`
- `Poetry`

### Установка

1. Создание виртуального окружения и установка зависимостей:
   ```commandline
   poetry install
   ```

2. Активация виртуального окружения:
   ```commandline
   poetry shell
   ```


### Запуск

1. Создание `.env` файла с необходимыми переменными:
   ```commandline
   make env
   ```

2. Создание базы в docker-контейнере (чтобы не работать с локальной базой):
   ```commandline
   make db
   ```

3. Выполнение миграций:
   ```commandline
   make migrate
   ```

4. Запуск приложения:
   ```commandline
   make run
   ```

