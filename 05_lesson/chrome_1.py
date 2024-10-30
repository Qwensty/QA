from selenium import webdriver
from time import sleep

# Инициализация драйвера Chrome
driver = webdriver.Chrome()

try:
    # Открыть страницу
    driver.get("http://the-internet.herokuapp.com/add_remove_elements/")

    # Найти кнопку "Add Element" и кликнуть на нее 5 раз
    add_button = driver.find_element("xpath", "//button[text()='Add Element']")
    for _ in range(5):
        add_button.click()
        sleep(5)  # Задержка для наглядности (опционально)

    # Собрать список кнопок "Delete" и вывести их количество
    delete_buttons = driver.find_elements("xpath", "//button[text()='Delete']")
    print(f"Количество кнопок Delete: {len(delete_buttons)}")

finally:
    driver.quit()