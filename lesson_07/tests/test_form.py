from selenium.webdriver.common.by import By

from lesson_07.pages.form_page import FormPage

def test_form(driver):
    form_page = FormPage(driver)
    form_page.open()

    data = {
        "firstname": "Иван",
        "lastname": "Петров",
        "address": "Ленина, 55-3",
        "email": "test@skypro.com",
        "phone": "+7985899998787",
        "city": "Москва",
        "country": "Россия",
        "job_position": "QA",
        "company": "SkyPro"
    }

    form_page.fill_form(data)
    form_page.submit()

    # Получаем цвета всех полей
    colors = form_page.get_all_fields_color()

    # Проверяем, что поле Zip code подсвечено красным
    assert colors["zip-code"] == "rgb(245, 194, 199)", "Zip code field is not red."

    # Проверяем, что остальные поля подсвечены зеленым
    for field in ["first-name", "last-name", "address", "e-mail", "phone", "city", "country", "job-position", "company"]:
        assert colors[field] == "rgb(186, 219, 204)", f"Field {field} is not green."
