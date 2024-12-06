import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DB_URI = "postgresql://postgres:1111@localhost:5432/QA"

@pytest.fixture(scope="module")
def db_session():
    # Создаём подключение к существующей базе данных
    engine = create_engine(DB_URI)
    Session = sessionmaker(bind=engine)
    session = Session()

    yield session  # Передаём сессию в тесты

    session.close()
