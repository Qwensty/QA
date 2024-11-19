from selenium.webdriver.common.by import By

class ShopPage:
    URL = "https://www.saucedemo.com/"

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get(self.URL)

    def login(self, username, password):
        self.driver.find_element(By.ID, "user-name").send_keys(username)
        self.driver.find_element(By.ID, "password").send_keys(password)
        self.driver.find_element(By.ID, "login-button").click()

    def add_to_cart(self, item_name):
        self.driver.find_element(By.XPATH, f"//div[text()='{item_name}']").click()
        self.driver.find_element(By.XPATH, "//button[text()='Add to cart']").click()
        self.driver.back()

    def go_to_cart(self):
        self.driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

    def checkout(self, first_name, last_name, zip_code):
        self.driver.find_element(By.ID, "checkout").click()
        self.driver.find_element(By.ID, "first-name").send_keys(first_name)
        self.driver.find_element(By.ID, "last-name").send_keys(last_name)
        self.driver.find_element(By.ID, "postal-code").send_keys(zip_code)
        self.driver.find_element(By.ID, "continue").click()

    def get_total(self):
        return self.driver.find_element(By.CLASS_NAME, "summary_total_label").text
