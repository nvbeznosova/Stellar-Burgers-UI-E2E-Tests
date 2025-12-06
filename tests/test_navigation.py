import allure
from pages.main_page import MainPage

@allure.suite("Навигация")
class TestNavigation:

    @allure.title("Переход по клику на Конструктор")
    def test_go_to_constructor(self, driver):
        page = MainPage(driver)
        page.go_to_constructor()
        assert page.is_visible(MainPage.CONSTRUCTOR_AREA)

    @allure.title("Переход по клику на Лента заказов")
    def test_go_to_order_feed(self, driver):
        page = MainPage(driver)
        page.go_to_order_feed()
        assert page.is_visible(MainPage.ORDER_FEED_LINK)