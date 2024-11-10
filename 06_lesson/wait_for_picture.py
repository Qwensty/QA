from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Инициализация веб-драйвера
driver = webdriver.Chrome()

try:
    # Переход на страницу
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")

    # Ожидание появления как минимум трёх изображений на странице
    WebDriverWait(driver, 50).until(
        lambda d: len(d.find_elements(By.TAG_NAME, 'img')) >= 5
    )

    # Теперь ждём, пока третье изображение получит атрибут 'src'
    third_image = WebDriverWait(driver, 30).until(
        lambda d: d.find_elements(By.TAG_NAME, 'img')[3].get_attribute('src')
    )

    # Получение и вывод значения атрибута 'src' у третьей картинки
    print("URL третьего изображения:", third_image)

finally:
    # Закрытие драйвера
    driver.quit()
