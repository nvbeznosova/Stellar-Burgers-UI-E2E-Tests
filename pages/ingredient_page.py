from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class IngredientPage(BasePage):
    MODAL = (By.XPATH, "//div[contains(@class,'Modal_modal__content')]")
    CLOSE_BTN = (By.XPATH, "//button[contains(@class,'Modal_modal__close')]")

    def is_modal_open(self):
        return self.is_visible(self.MODAL)

    def close_modal(self):
        self.click(self.CLOSE_BTN)