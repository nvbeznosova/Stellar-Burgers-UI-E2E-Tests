from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from pages.base_page import BasePage

class MainPage(BasePage):
    CONSTRUCTOR_BTN = (By.XPATH, "//a[text()='Конструктор']")
    ORDER_FEED_BTN = (By.XPATH, "//a[text()='Лента заказов']")
    INGREDIENT = (By.CSS_SELECTOR, ".BurgerIngredient_card__3-4-1")
    INGREDIENT_COUNTER = (By.CSS_SELECTOR, ".counter_counter__num__3nue1")
    CONSTRUCTOR_AREA = (By.CSS_SELECTOR, ".BurgerConstructor_constructor__area__2jX7-")
    ORDER_BTN = (By.XPATH, "//button[text()='Оформить заказ']")
    ORDER_MODAL = (By.CSS_SELECTOR, ".Modal_modal__content__1QYj-")

    def go_to_constructor(self):
        self.click(self.CONSTRUCTOR_BTN)

    def go_to_order_feed(self):
        self.click(self.ORDER_FEED_BTN)

    def open_ingredient(self):
        self.click(self.INGREDIENT)

    def add_ingredient(self):
        self.click(self.INGREDIENT)

    def get_counter_value(self):
        return int(self.get_text(self.INGREDIENT_COUNTER))

    def drag_ingredient_to_constructor(self):
        ingredient = self.driver.find_element(*self.INGREDIENT)
        target = self.driver.find_element(*self.CONSTRUCTOR_AREA)
        ActionChains(self.driver).drag_and_drop(ingredient, target).perform()

    def click_order_button(self):
        self.click(self.ORDER_BTN)

    def is_order_modal_open(self):
        return self.is_visible(self.ORDER_MODAL)