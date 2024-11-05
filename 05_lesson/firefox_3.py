from selenium import webdriver
from time import sleep

# Инициализация драйвера Firefox
driver = webdriver.Firefox()

try:
    # Открыть страницу
    driver.get("http://the-internet.herokuapp.com/login")

    # Ввести логин
    username = driver.find_element("id", "username")
    username.send_keys("tomsmith")

    # Ввести пароль
    password = driver.find_element("id", "password")
    password.send_keys("SuperSecretPassword!")

    # Нажать кнопку "Login"
    login_button = driver.find_element("xpath", "//button[@type='submit']")
    login_button.click()

finally:
    driver.quit()
