from selenium import webdriver

# Инициализация драйвера Chrome
driver = webdriver.Chrome()

try:
    # Открыть страницу
    driver.get("http://uitestingplayground.com/dynamicid")

    # Кликнуть по синей кнопке (используем текст)
    button = driver.find_element("xpath", "//button[text()='Button with Dynamic ID']")
    button.click()

finally:
    driver.quit()