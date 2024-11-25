from lesson_07.pages.shop_page import ShopPage


def test_shop(driver):
    shop_page = ShopPage(driver)
    shop_page.open()

    shop_page.login("standard_user", "secret_sauce")
    shop_page.add_to_cart("Sauce Labs Backpack")
    shop_page.add_to_cart("Sauce Labs Bolt T-Shirt")
    shop_page.add_to_cart("Sauce Labs Onesie")

    shop_page.go_to_cart()
    shop_page.checkout("Иван", "Петров", "123456")

    total = shop_page.get_total()
    assert total.endswith("$58.29")  # Проверка на окончание строки

