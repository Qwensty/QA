#Файл для проверки подключения к БД
from sqlalchemy import create_engine

# Строка подключения
DB_URI = "postgresql://postgres:1111@localhost:5432/QA"

# Создание подключения
engine = create_engine(DB_URI)

# Проверка подключения
with engine.connect() as connection:
    print("Подключение к базе данных успешно!")
