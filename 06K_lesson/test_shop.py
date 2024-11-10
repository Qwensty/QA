from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
#Запись для обновления commit
# Инициализация веб-драйвера
driver = webdriver.Chrome()

try:
    # Переход на страницу
    driver.get("https://www.saucedemo.com/")

    # Авторизация
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    # Добавление товаров в корзину
    driver.find_element(By.XPATH, "//div[text()='Sauce Labs Backpack']").click()
    driver.find_element(By.XPATH, "//button[text()='Add to cart']").click()
    driver.back()

    driver.find_element(By.XPATH, "//div[text()='Sauce Labs Bolt T-Shirt']").click()
    driver.find_element(By.XPATH, "//button[text()='Add to cart']").click()
    driver.back()

    driver.find_element(By.XPATH, "//div[text()='Sauce Labs Onesie']").click()
    driver.find_element(By.XPATH, "//button[text()='Add to cart']").click()

    # Переход в корзину
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

    # Переход к оформлению заказа (Checkout)
    driver.find_element(By.ID, "checkout").click()

    # Заполнение формы
    driver.find_element(By.ID, "first-name").send_keys("Руслан")
    driver.find_element(By.ID, "last-name").send_keys("Баранов")
    driver.find_element(By.ID, "postal-code").send_keys("230000")
    driver.find_element(By.ID, "continue").click()

    # Получение и проверка итоговой суммы
    total_text = WebDriverWait(driver, 30).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "summary_total_label"))
    ).text
    assert "$58.29" in total_text, "Итоговая сумма неверна"

finally:
    driver.quit()
