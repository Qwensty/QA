import pytest
from StringUtils import StringUtils


utils = StringUtils()


# 1. Тестирование метода 'capitilize'
def test_capitilize():
    # Позитивные тест-кейсы
    assert utils.capitilize("skypro") == "Skypro"
    assert utils.capitilize("hello") == "Hello"

    # Негативные тест-кейсы
    assert utils.capitilize("") == ""  # Проверка на пустую строку
    assert utils.capitilize("123abc") == "123abc"  # Нет букв для преобразования


# 2. Тестирование метода 'trim'
def test_trim():
    # Позитивные тест-кейсы
    assert utils.trim("   skypro") == "skypro"
    assert utils.trim("no spaces") == "no spaces"

    # Негативные тест-кейсы
    assert utils.trim("") == ""  # Проверка на пустую строку
    assert utils.trim("   ") == ""  # Проверка на строку, состоящую только из пробелов


# 3. Тестирование метода 'to_list'
def test_to_list():
    # Позитивные тест-кейсы
    assert utils.to_list("a,b,c,d") == ["a", "b", "c", "d"]
    assert utils.to_list("1:2:3", ":") == ["1", "2", "3"]

    # Негативные тест-кейсы
    assert utils.to_list("") == []  # Пустая строка должна вернуть пустой список
    assert utils.to_list("1,2,3", ":") == ["1,2,3"]  # Неверный разделитель


# 4. Тестирование метода 'contains'
def test_contains():
    # Позитивные тест-кейсы
    assert utils.contains("SkyPro", "S") == True
    assert utils.contains("Hello", "o") == True

    # Негативные тест-кейсы
    assert utils.contains("SkyPro", "U") == False
    assert utils.contains("", "S") == False  # Пустая строка


# 5. Тестирование метода 'delete_symbol'
def test_delete_symbol():
    # Позитивные тест-кейсы
    assert utils.delete_symbol("SkyPro", "k") == "SyPro"
    assert utils.delete_symbol("SkyPro", "Pro") == "Sky"

    # Негативные тест-кейсы
    assert utils.delete_symbol("SkyPro", "X") == "SkyPro"  # Символ не найден
    assert utils.delete_symbol("", "S") == ""  # Пустая строка


# 6. Тестирование метода 'starts_with'
def test_starts_with():
    # Позитивные тест-кейсы
    assert utils.starts_with("SkyPro", "S") == True
    assert utils.starts_with("SkyPro", "Sky") == True

    # Негативные тест-кейсы
    assert utils.starts_with("SkyPro", "P") == False
    assert utils.starts_with("", "S") == False  # Пустая строка


# 7. Тестирование метода 'end_with'
def test_end_with():
    # Позитивные тест-кейсы
    assert utils.end_with("SkyPro", "o") == True
    assert utils.end_with("SkyPro", "Pro") == True

    # Негативные тест-кейсы
    assert utils.end_with("SkyPro", "S") == False
    assert utils.end_with("", "o") == False  # Пустая строка


# 8. Тестирование метода 'is_empty'
def test_is_empty():
    # Позитивные тест-кейсы
    assert utils.is_empty("") == True
    assert utils.is_empty(" ") == True  # Пробелы должны считаться пустыми

    # Негативные тест-кейсы
    assert utils.is_empty("SkyPro") == False
    assert utils.is_empty("   sky") == False


# 9. Тестирование метода 'list_to_string'
def test_list_to_string():
    # Позитивные тест-кейсы
    assert utils.list_to_string([1, 2, 3, 4]) == "1, 2, 3, 4"
    assert utils.list_to_string(["Sky", "Pro"]) == "Sky, Pro"
    assert utils.list_to_string(["Sky", "Pro"], "-") == "Sky-Pro"

    # Негативные тест-кейсы
    assert utils.list_to_string([]) == ""  # Пустой список
    assert utils.list_to_string([1]) == "1"  # Список с одним элементом