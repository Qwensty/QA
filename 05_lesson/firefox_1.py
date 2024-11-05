from selenium import webdriver
from time import sleep

# Инициализация драйвера Firefox
driver = webdriver.Firefox()

try:
    # Открыть страницу
    driver.get("http://the-internet.herokuapp.com/entry_ad")

    # Подождать, пока загрузится модальное окно
    sleep(10)

    # Найти и кликнуть на кнопку "Close" в модальном окне
    close_button = driver.find_element("xpath", "//div[@class='modal-footer']/p[text()='Close']")
    close_button.click()

finally:
    driver.quit()