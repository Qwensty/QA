from selenium.webdriver.common.by import By

from lesson_07.pages.form_page import FormPage

def test_form(driver):
    form_page = FormPage(driver)
    form_page.open()

    data = {
        "first_name": "Иван",
        "last_name": "Петров",
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

    assert "alert py-2 alert-danger" in form_page.get_field_class("zip-code")
    for field_id in ["first-name", "last-name", "address", "e-mail", "phone", "city", "country", "job-position",
                     "company"]:
        field = driver.find_element(By.ID, field_id)
        field_class = field.get_attribute("class")
