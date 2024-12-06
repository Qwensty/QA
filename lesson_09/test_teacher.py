from lesson_09.models import Teacher


def test_add_teacher(db_session):
    """Тест добавления преподавателя."""
    new_teacher = Teacher(email="teacher1@example.com", group_id=1)
    db_session.add(new_teacher)
    db_session.commit()

    # Проверяем, что запись добавлена
    added_teacher = db_session.query(Teacher).filter_by(email="teacher1@example.com").first()
    assert added_teacher is not None
    assert added_teacher.group_id == 1

    # Удаляем данные после теста
    db_session.delete(added_teacher)
    db_session.commit()

def test_update_teacher(db_session):
    """Тест обновления данных преподавателя."""
    teacher = Teacher(email="teacher2@example.com", group_id=1)
    db_session.add(teacher)
    db_session.commit()

    # Обновляем данные
    teacher.group_id = 2
    db_session.commit()

    # Проверяем изменения
    updated_teacher = db_session.query(Teacher).filter_by(email="teacher2@example.com").first()
    assert updated_teacher.group_id == 2

    # Удаляем данные после теста
    db_session.delete(updated_teacher)
    db_session.commit()

def test_delete_teacher(db_session):
    """Тест удаления преподавателя."""
    teacher = Teacher(email="teacher3@example.com", group_id=1)
    db_session.add(teacher)
    db_session.commit()

    # Удаляем запись
    db_session.delete(teacher)
    db_session.commit()

    # Проверяем, что запись удалена
    deleted_teacher = db_session.query(Teacher).filter_by(email="teacher3@example.com").first()
    assert deleted_teacher is None

