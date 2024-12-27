from flask import Flask

app = Flask(__name__)
app.secret_key = "your_secret_key"  # Секретный ключ для сессий

from app import routes  # Подключение маршрутов