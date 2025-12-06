from selenium.webdriver.common.by import By
from pages.base_page import BasePage
import allure

class OrderFeedPage(BasePage):
    TOTAL_COUNTER = (By.XPATH, "//p[text()='Выполнено за все время:']/following-sibling::p")
    TODAY_COUNTER = (By.XPATH, "//p[text()='Выполнено за сегодня:']/following-sibling::p")
    IN_PROGRESS_ORDERS = (By.XPATH, "//ul[contains(@class,'OrderFeed_orderList')]/li")

    @allure.step("Получаем общее число выполненных заказов за всё время")
    def get_total_count(self):
        text = self.get_text(self.TOTAL_COUNTER)
        return int(text) if text.isdigit() else 0

    @allure.step("Получаем число выполненных заказов за сегодня")
    def get_today_count(self):
        text = self.get_text(self.TODAY_COUNTER)
        return int(text) if text.isdigit() else 0

    @allure.step("Получаем список заказов в работе")
    def get_in_progress_orders(self):
        orders = self.find_all(self.IN_PROGRESS_ORDERS)
        return [o.text for o in orders if o.text]