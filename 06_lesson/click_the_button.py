from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Инициализация веб-драйвера
driver = webdriver.Chrome()

# Переход на страницу
driver.get("http://uitestingplayground.com/ajax")

# Нажатие на синюю кнопку
button = driver.find_element(By.CSS_SELECTOR, 'button#ajaxButton')
button.click()

# Ожидание появления текста в зеленой плашке
text_element = WebDriverWait(driver, 20).until(
    EC.visibility_of_element_located((By.CSS_SELECTOR, '.bg-success'))
)

# Получение текста и вывод в консоль
print(text_element.text)

# Закрытие драйвера
driver.quit()
