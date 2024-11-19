from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from lesson_07.pages.calculator_page import CalculatorPage


def test_calculator(driver):
    calc_page = CalculatorPage(driver)
    calc_page.open()

    calc_page.set_delay("45")
    calc_page.press_button("7")
    calc_page.press_button("+")
    calc_page.press_button("8")
    calc_page.press_button("=")

    # Ожидание появления результата
    WebDriverWait(driver, 50).until(
        EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".screen"), "15")
    )

    result = calc_page.get_result()
    assert result == "15"

