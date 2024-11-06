from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Инициализация веб-драйвера
driver = webdriver.Chrome()

# Переход на страницу
driver.get("https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")

# Ожидание загрузки всех изображений
WebDriverWait(driver, 10).until(
    EC.presence_of_all_elements_located((By.TAG_NAME, 'img'))
)

# Получение значения атрибута 'src' у третьей картинки
third_image = driver.find_elements(By.TAG_NAME, 'img')[2]
print(third_image.get_attribute('src'))

# Закрытие драйвера
driver.quit()
