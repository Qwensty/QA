from selenium.webdriver.common.by import By

class FormPage:
    URL = "https://bonigarcia.dev/selenium-webdriver-java/data-types.html"

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get(self.URL)

    def fill_form(self, data):
        self.driver.find_element(By.NAME, "first-name").send_keys(data["first_name"])
        self.driver.find_element(By.NAME, "last-name").send_keys(data["last_name"])
        self.driver.find_element(By.NAME, "address").send_keys(data["address"])
        self.driver.find_element(By.NAME, "e-mail").send_keys(data["email"])
        self.driver.find_element(By.NAME, "phone").send_keys(data["phone"])
        self.driver.find_element(By.NAME, "city").send_keys(data["city"])
        self.driver.find_element(By.NAME, "country").send_keys(data["country"])
        self.driver.find_element(By.NAME, "job-position").send_keys(data["job_position"])
        self.driver.find_element(By.NAME, "company").send_keys(data["company"])

    def submit(self):
        self.driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

    def get_field_class(self, field_id):
        return self.driver.find_element(By.ID, field_id).get_attribute("class")
