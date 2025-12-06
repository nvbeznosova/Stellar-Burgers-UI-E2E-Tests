import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.login_page import LoginPage
from pages.main_page import MainPage

@allure.suite("Оформление заказа")
class TestOrderForm:

    @allure.title("Модальное окно заказа содержит текст 'заказ'")
    def test_order_modal_has_text(self, driver):
        login = LoginPage(driver)
        login.open_login_form()
        login.login("fedya@yandex.ru", "Fedya2025")

        WebDriverWait(driver, 30).until(EC.visibility_of_element_located(MainPage.CONSTRUCTOR_AREA))

        main = MainPage(driver)
        main.drag_ingredient_to_constructor()
        main.click_order_button()

        WebDriverWait(driver, 45).until(EC.visibility_of_element_located(MainPage.ORDER_MODAL))
        assert main.is_order_modal_open()

        modal_text = main.get_text(MainPage.ORDER_MODAL).lower()
        assert "заказ" in modal_text