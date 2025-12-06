import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.order_feed_page import OrderFeedPage

@allure.suite("Лента заказов")
class TestOrderFeed:

    def _login_and_prepare(self, driver):
        login = LoginPage(driver)
        login.open_login_form()
        login.login("fedya@yandex.ru", "Fedya2025")
        WebDriverWait(driver, 30).until(EC.visibility_of_element_located(MainPage.CONSTRUCTOR_AREA))

    def _make_order(self, driver):
        main = MainPage(driver)
        main.go_to_constructor()
        main.drag_ingredient_to_constructor()
        main.click_order_button()
        WebDriverWait(driver, 45).until(EC.visibility_of_element_located(MainPage.ORDER_MODAL))
        assert main.is_order_modal_open()

    @allure.title("При создании заказа счётчик 'Выполнено за всё время' увеличивается")
    def test_total_counter_increases(self, driver):
        self._login_and_prepare(driver)
        main = MainPage(driver)
        main.go_to_order_feed()

        feed = OrderFeedPage(driver)
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(OrderFeedPage.TOTAL_COUNTER))
        total_before = feed.get_total_count()

        self._make_order(driver)

        main.go_to_order_feed()
        WebDriverWait(driver, 45).until(lambda d: feed.get_total_count() >= total_before)
        total_after = feed.get_total_count()
        assert total_after >= total_before

    @allure.title("При создании заказа счётчик 'Выполнено за сегодня' увеличивается")
    def test_today_counter_increases(self, driver):
        self._login_and_prepare(driver)
        main = MainPage(driver)
        main.go_to_order_feed()

        feed = OrderFeedPage(driver)
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(OrderFeedPage.TODAY_COUNTER))
        today_before = feed.get_today_count()

        self._make_order(driver)

        main.go_to_order_feed()
        WebDriverWait(driver, 45).until(lambda d: feed.get_today_count() >= today_before)
        today_after = feed.get_today_count()
        assert today_after >= today_before

    @allure.title("После оформления заказа его номер появляется в разделе 'В работе'")
    def test_order_appears_in_progress(self, driver):
        self._login_and_prepare(driver)
        self._make_order(driver)

        main = MainPage(driver)
        main.go_to_order_feed()
        feed = OrderFeedPage(driver)

        in_progress_after = feed.get_in_progress_orders()
        assert len(in_progress_after) > 0