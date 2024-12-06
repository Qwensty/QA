import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from lesson_10.pages.calculator_page import CalculatorPage

@allure.feature("Калькулятор")
@allure.story("Медленный калькулятор")
@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Тест работы медленного калькулятора")
@allure.description("Проверяет корректность вычислений при использовании медленного калькулятора.")
def test_calculator(driver):
    calc_page = CalculatorPage(driver)

    with allure.step("Открыть страницу калькулятора"):
        calc_page.open()

    with allure.step("Установить задержку вычислений"):
        calc_page.set_delay("45")

    with allure.step("Выполнить вычисление 7 + 8"):
        calc_page.press_button("7")
        calc_page.press_button("+")
        calc_page.press_button("8")
        calc_page.press_button("=")

    with allure.step("Дождаться результата вычисления"):
        WebDriverWait(driver, 50).until(
            EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".screen"), "15")
        )
        result = calc_page.get_result()

    with allure.step("Проверить результат вычисления"):
        allure.attach(result, "Результат вычислений", allure.attachment_type.TEXT)
        assert result == "15", f"Expected result '15', got '{result}'"
