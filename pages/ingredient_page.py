from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class IngredientPage(BasePage):
    MODAL = (By.CSS_SELECTOR, ".Modal_modal__content__1QYj-")
    CLOSE_BTN = (By.CSS_SELECTOR, ".Modal_modal__close__3-4-1")

    def is_modal_open(self):
        return self.is_visible(self.MODAL)

    def close_modal(self):
        self.click(self.CLOSE_BTN)