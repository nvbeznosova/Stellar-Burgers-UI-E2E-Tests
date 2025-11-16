from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class OrderFeedPage(BasePage):
    TOTAL_COUNTER = (By.XPATH, "//p[text()='Выполнено за всё время']/following-sibling::p")
    TODAY_COUNTER = (By.XPATH, "//p[text()='Выполнено за сегодня']/following-sibling::p")
    IN_PROGRESS = (By.CSS_SELECTOR, ".OrderFeed_inProgress__list")

    def get_total_count(self):
        return int(self.get_text(self.TOTAL_COUNTER))

    def get_today_count(self):
        return int(self.get_text(self.TODAY_COUNTER))

    def get_in_progress_orders(self):
        return self.get_text(self.IN_PROGRESS)