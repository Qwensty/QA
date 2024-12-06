import allure
from selenium.webdriver.common.by import By

class CalculatorPage:
    """Класс для работы с калькулятором."""
    URL = "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"

    def __init__(self, driver):
        """
        Инициализация класса.

        :param driver: WebDriver, используемый для работы с браузером.
        """
        self.driver = driver

    @allure.step("Открыть страницу калькулятора")
    def open(self) -> None:
        """Открывает страницу калькулятора."""
        self.driver.get(self.URL)

    @allure.step("Установить задержку: {value}")
    def set_delay(self, value: str) -> None:
        """
        Устанавливает задержку выполнения операций.

        :param value: Время задержки в секундах.
        """
        delay_input = self.driver.find_element(By.ID, "delay")
        delay_input.clear()
        delay_input.send_keys(value)

    @allure.step("Нажать кнопку: {button}")
    def press_button(self, button: str) -> None:
        """
        Нажимает указанную кнопку.

        :param button: Символ кнопки.
        """
        self.driver.find_element(By.XPATH, f"//span[text()='{button}']").click()

    @allure.step("Получить результат")
    def get_result(self) -> str:
        """
        Возвращает результат вычислений.

        :return: Результат в виде строки.
        """
        return self.driver.find_element(By.CSS_SELECTOR, ".screen").text
