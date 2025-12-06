from selenium.webdriver.common.by import By
from pages.base_page import BasePage
import allure

class MainPage(BasePage):
    CONSTRUCTOR_LINK = (By.XPATH, "//a[@href='/' and .//p[text()='Конструктор']]")
    ORDER_FEED_LINK = (By.XPATH, "//a[@href='/feed' and .//p[text()='Лента Заказов']]")
    LOGIN_ACCOUNT_BTN = (By.XPATH, "//button[text()='Войти в аккаунт']")

    INGREDIENT = (By.XPATH, "//a[contains(@class,'BurgerIngredient_ingredient__')]")
    INGREDIENT_COUNTER = (By.XPATH, "//p[contains(@class,'counter_counter__num__')]")

    CONSTRUCTOR_AREA = (By.XPATH, "//section[contains(@class,'BurgerConstructor_basket__')]")
    ORDER_BTN = (By.XPATH, "//button[text()='Оформить заказ']")

    ORDER_MODAL = (By.XPATH, "//section[contains(@class,'Modal_modal_opened__')]")
    ORDER_MODAL_CLOSE = (By.XPATH, "//section[contains(@class,'Modal_modal_opened__')]//button")
    ORDER_NUMBER = (By.XPATH, "//section[contains(@class,'Modal_modal_opened__')]//h2")

    @allure.step("Переходим в раздел Конструктор")
    def go_to_constructor(self):
        self.safe_click(self.CONSTRUCTOR_LINK)

    @allure.step("Переходим в раздел Лента заказов")
    def go_to_order_feed(self):
        if self.is_visible(self.ORDER_MODAL):
            self.safe_click(self.ORDER_MODAL_CLOSE)
            self.wait_invisible(self.ORDER_MODAL)
        self.safe_click(self.ORDER_FEED_LINK)

    @allure.step("Открываем первый ингредиент")
    def open_ingredient(self):
        self.click(self.INGREDIENT)

    @allure.step("Получаем значение счётчика ингредиента")
    def get_counter_value(self):
        text = self.get_text(self.INGREDIENT_COUNTER)
        return int(text) if text.isdigit() else 0

    @allure.step("Перетаскиваем ингредиент в конструктор")
    def drag_ingredient_to_constructor(self):
        self.drag_and_drop(self.INGREDIENT, self.CONSTRUCTOR_AREA)

    @allure.step("Нажимаем кнопку Оформить заказ")
    def click_order_button(self):
        self.click(self.ORDER_BTN)

    @allure.step("Проверяем, что модальное окно заказа открыто")
    def is_order_modal_open(self):
        return self.is_visible(self.ORDER_MODAL)

    @allure.step("Получаем номер заказа")
    def get_order_number(self):
        return self.get_text(self.ORDER_NUMBER)