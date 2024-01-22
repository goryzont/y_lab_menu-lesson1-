# Запуск проекта

1.Склонируйте репозиторий git clone https://github.com/goryzont/y_lab_menu-lesson1-  /n
2.Подготовьте базу данных (PostgreSQL) создайте пользователя, создайте базу данных /n
3.Создайте файл .env в дериктории проекта и заполните его по примеру файла .env /n
4.Создайте виртуальное окружение в дериктории проекта и активируйте его: /n
```
python -m venv venv
source venv/bin/activate
```

5.Установите все зависимости
```
pip install -r requirements.txt
```

6.Примените миграцию
```
alembic upgrade head
```
7.Запустите сервер 
```
uvicorn app.main:app --reload```
```
