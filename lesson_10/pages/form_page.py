import allure
from selenium.webdriver.common.by import By

class FormPage:
    """Класс для взаимодействия с формой."""
    URL = "https://bonigarcia.dev/selenium-webdriver-java/data-types.html"

    def __init__(self, driver):
        """
        Инициализация класса.

        :param driver: WebDriver, используемый для работы с браузером.
        """
        self.driver = driver

    @allure.step("Открыть страницу формы")
    def open(self) -> None:
        """Открывает страницу формы."""
        self.driver.get(self.URL)

    @allure.step("Заполнить форму данными")
    def fill_form(self, data: dict) -> None:
        """
        Заполняет форму данными.

        :param data: Словарь с данными для заполнения формы.
        """
        self.driver.find_element(By.NAME, "first-name").send_keys(data["firstname"])
        self.driver.find_element(By.NAME, "last-name").send_keys(data["lastname"])
        self.driver.find_element(By.NAME, "address").send_keys(data["address"])
        self.driver.find_element(By.NAME, "e-mail").send_keys(data["email"])
        self.driver.find_element(By.NAME, "phone").send_keys(data["phone"])
        self.driver.find_element(By.NAME, "city").send_keys(data["city"])
        self.driver.find_element(By.NAME, "country").send_keys(data["country"])
        self.driver.find_element(By.NAME, "job-position").send_keys(data["job_position"])
        self.driver.find_element(By.NAME, "company").send_keys(data["company"])

    @allure.step("Отправить форму")
    def submit(self) -> None:
        """Нажимает кнопку отправки формы."""
        self.driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

    @allure.step("Получить цвет поля {field_name}")
    def get_field_color(self, field_name: str) -> str:
        """
        Возвращает цвет обводки поля.

        :param field_name: Имя поля.
        :return: Цвет обводки поля в формате RGB.
        """
        field = self.driver.find_element(By.ID, field_name)
        return field.value_of_css_property("border-color")

    @allure.step("Получить цвета всех полей формы")
    def get_all_fields_color(self) -> dict:
        """
        Возвращает цвета всех полей формы.

        :return: Словарь с цветами обводки для каждого поля.
        """
        fields = [
            "first-name", "last-name", "address", "e-mail", "phone", "zip-code",
            "city", "country", "job-position", "company"
        ]
        field_colors = {}
        for field in fields:
            field_colors[field] = self.get_field_color(field)
        return field_colors

