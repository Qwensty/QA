from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
#Запись для обновления commit
# Инициализация веб-драйвера
def test_form():

    driver = webdriver.Chrome()

    try:
        # Переход на страницу
        driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

        # Установление времени ожидания элементов
        wait = WebDriverWait(driver, 30)

        # Заполнение формы с ожиданием каждого элемента
        wait.until(EC.presence_of_element_located((By.NAME, "first-name"))).send_keys("Иван")
        wait.until(EC.presence_of_element_located((By.NAME, "last-name"))).send_keys("Петров")
        wait.until(EC.presence_of_element_located((By.NAME, "address"))).send_keys("Ленина, 55-3")
        wait.until(EC.presence_of_element_located((By.NAME, "e-mail"))).send_keys("test@skypro.com")
        wait.until(EC.presence_of_element_located((By.NAME, "phone"))).send_keys("+7985899998787")
        wait.until(EC.presence_of_element_located((By.NAME, "city"))).send_keys("Москва")
        wait.until(EC.presence_of_element_located((By.NAME, "country"))).send_keys("Россия")
        wait.until(EC.presence_of_element_located((By.NAME, "job-position"))).send_keys("QA")
        wait.until(EC.presence_of_element_located((By.NAME, "company"))).send_keys("SkyPro")

        # Нажатие на кнопку Submit
        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))).click()

        # Добавление дополнительного ожидания после нажатия Submit
        wait.until(EC.presence_of_element_located((By.ID, "zip-code")))

        # Ожидание, что поле zip-code будет отображено
        zip_code_field = wait.until(EC.presence_of_element_located((By.ID, "zip-code")))

        # Проверка наличия классов "alert py-2 alert-danger"
        assert "alert py-2 alert-danger" in zip_code_field.get_attribute("class"), "Поле zip-code не подсвечено красным"

        # Проверка остальных полей
        for field_id in ["first-name", "last-name", "address", "e-mail", "phone", "city", "country", "job-position",
                         "company"]:
            field = driver.find_element(By.ID, field_id)
            field_class = field.get_attribute("class")

    finally:
        driver.quit()