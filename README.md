# Web Auction

```cd backend``` - переходим на директорию бекенда

```pip install -r requirements.txt``` - устанавливаем все зависимости 

```docker run -p 6379:6379 -d redis:5``` - запускаем Redis на Docker

В файле .env.example устанавливаем секретный ключ и DEBUG=True, переименовываем файл в просто .env

```python manage.py migrate``` - делаем миграции

```python manage.py createsuperuser``` - создаём суперюзера

```python manage.py runserver``` - запускаем сервер

```npm install``` - устанавливаем все зависимости для фронтенда

```npm run dev``` - запускаем фронтенд
