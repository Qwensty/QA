from selenium import webdriver
from time import sleep

# Инициализация драйвера Firefox
driver = webdriver.Firefox()

try:
    # Открыть страницу
    driver.get("http://the-internet.herokuapp.com/inputs")

    # Найти поле ввода, ввести 1000, затем очистить и ввести 999
    input_field = driver.find_element("tag name", "input")
    input_field.send_keys("1000")
    sleep(10)
    input_field.clear()
    input_field.send_keys("999")

finally:
    driver.quit()