from selenium.webdriver.common.by import By
from pages.base_page import BasePage
import allure

class IngredientPage(BasePage):
    MODAL = (By.XPATH, "//div[contains(@class,'Modal_modal__content')]")
    CLOSE_BTN = (By.XPATH, "//button[contains(@class,'Modal_modal__close')]")

    @allure.step("Проверяем, что модальное окно ингредиента открыто")
    def is_modal_open(self):
        return self.is_visible(self.MODAL)

    @allure.step("Закрываем модальное окно ингредиента")
    def close_modal(self):
        self.click(self.CLOSE_BTN)