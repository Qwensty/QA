import allure
from selenium.webdriver.common.by import By

class ShopPage:
    """Класс для взаимодействия с магазином."""
    URL = "https://www.saucedemo.com/"

    def __init__(self, driver):
        """
        Инициализация класса.

        :param driver: WebDriver, используемый для работы с браузером.
        """
        self.driver = driver

    @allure.step("Открыть магазин")
    def open(self) -> None:
        """Открывает магазин."""
        self.driver.get(self.URL)

    @allure.step("Авторизоваться с логином: {username}")
    def login(self, username: str, password: str) -> None:
        """
        Выполняет вход в систему.

        :param username: Логин пользователя.
        :param password: Пароль пользователя.
        """
        self.driver.find_element(By.ID, "user-name").send_keys(username)
        self.driver.find_element(By.ID, "password").send_keys(password)
        self.driver.find_element(By.ID, "login-button").click()

    @allure.step("Добавить товар в корзину: {item_name}")
    def add_to_cart(self, item_name: str) -> None:
        """
        Добавляет товар в корзину.

        :param item_name: Название товара.
        """
        self.driver.find_element(By.XPATH, f"//div[text()='{item_name}']").click()
        self.driver.find_element(By.XPATH, "//button[text()='Add to cart']").click()
        self.driver.back()

    @allure.step("Перейти в корзину")
    def go_to_cart(self) -> None:
        """Открывает корзину."""
        self.driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

    @allure.step("Оформить заказ с данными: {first_name}, {last_name}, {zip_code}")
    def checkout(self, first_name: str, last_name: str, zip_code: str) -> None:
        """
        Заполняет данные для оформления заказа.

        :param first_name: Имя.
        :param last_name: Фамилия.
        :param zip_code: Почтовый индекс.
        """
        self.driver.find_element(By.ID, "checkout").click()
        self.driver.find_element(By.ID, "first-name").send_keys(first_name)
        self.driver.find_element(By.ID, "last-name").send_keys(last_name)
        self.driver.find_element(By.ID, "postal-code").send_keys(zip_code)
        self.driver.find_element(By.ID, "continue").click()

    @allure.step("Получить итоговую сумму")
    def get_total(self) -> str:
        """
        Возвращает общую стоимость заказа.

        :return: Итоговая сумма.
        """
        return self.driver.find_element(By.CLASS_NAME, "summary_total_label").text

