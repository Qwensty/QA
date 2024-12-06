import allure
from lesson_10.pages.form_page import FormPage

@allure.feature("Форма")
@allure.story("Проверка отправки формы")
@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Тест валидации формы")
@allure.description("Проверяет цвета обводки полей после отправки формы.")
def test_form(driver):
    form_page = FormPage(driver)

    with allure.step("Открыть страницу формы"):
        form_page.open()

    with allure.step("Заполнить форму валидными данными"):
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

    with allure.step("Проверить цвета полей"):
        colors = form_page.get_all_fields_color()
        allure.attach(str(colors), "Цвета полей", allure.attachment_type.JSON)

        assert colors["zip-code"] == "rgb(245, 194, 199)", "Zip code field is not red."
        for field, color in colors.items():
            if field != "zip-code":
                assert color == "rgb(186, 219, 204)", f"{field} is not green."
