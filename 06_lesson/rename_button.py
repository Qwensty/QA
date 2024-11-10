from selenium import webdriver
from selenium.webdriver.common.by import By

# Инициализация веб-драйвера
driver = webdriver.Chrome()

# Переход на страницу
driver.get("http://uitestingplayground.com/textinput")

# Ввод текста "SkyPro" в поле
input_field = driver.find_element(By.CSS_SELECTOR, 'input#newButtonName')
input_field.send_keys("SkyPro")

# Нажатие на синюю кнопку
button = driver.find_element(By.CSS_SELECTOR, 'button#updatingButton')
button.click()

# Получение текста кнопки и вывод в консоль
print(button.text)

# Закрытие драйвера
driver.quit()
