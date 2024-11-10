from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Инициализация веб-драйвера
driver = webdriver.Chrome()

try:
    # Переход на страницу
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

    # Установление времени ожидания элементов
    wait = WebDriverWait(driver, 20)

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

    # Ожидание, что поле Zip code будет отображено и подсвечено красным
    zip_code_field = wait.until(
        EC.presence_of_element_located((By.NAME, "zip-code")))
    assert "is-invalid" in zip_code_field.get_attribute("class")

    # Проверка остальных полей
    for field_id in ["first-name", "last-name", "address", "email", "phone", "city", "country", "job-position",
                     "company"]:
        assert "is-valid" in driver.find_element(By.ID, field_id).get_attribute("class")

finally:
    driver.quit()