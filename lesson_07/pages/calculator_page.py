from selenium.webdriver.common.by import By

class CalculatorPage:
    URL = "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get(self.URL)

    def set_delay(self, value):
        delay_input = self.driver.find_element(By.ID, "delay")
        delay_input.clear()
        delay_input.send_keys(value)

    def press_button(self, button):
        self.driver.find_element(By.XPATH, f"//span[text()='{button}']").click()

    def get_result(self):
        return self.driver.find_element(By.CSS_SELECTOR, ".screen").text
