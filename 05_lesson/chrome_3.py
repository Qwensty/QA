from selenium import webdriver

# Инициализация драйвера Chrome
driver = webdriver.Chrome()

try:
    # Открыть страницу
    driver.get("http://uitestingplayground.com/classattr")

    # Клик по кнопке с классом 'btn-primary' и текстом 'Button'
    button = driver.find_element("xpath", "//button[contains(@class, 'btn-primary') and text()='Button']")
    button.click()

    # Принятие алерта
    alert = driver.switch_to.alert
    alert.accept()

finally:
    driver.quit()