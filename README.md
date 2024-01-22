Запуск проекта
<hr>
1.Склонируйте репозиторий git clone https://github.com/goryzont/y_lab_menu-lesson1-
2.Подготовьте базу данных (PostgreSQL) создайте пользователя, создайте базу данных
3.Создайте файл .env в дериктории проекта и заполните его по примеру файла .env
4.Создайте виртуальное окружение в дериктории проекта и активируйте его:
python -m venv venv
source venv/bin/activate

5.Установите все зависимости
pip install -r requirements.txt

6.Примените миграцию
alembic upgrade head

7.Запустите сервер 
uvicorn app.main:app --reload
