from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class LoginPage(BasePage):
    EMAIL_INPUT = (By.NAME, "fedya@yandex.ru")
    PASSWORD_INPUT = (By.NAME, "Fedya2025")
    LOGIN_BTN = (By.XPATH, "//button[text()='Войти']")

    def login(self, email, password):
        # Вводим email
        self.driver.find_element(*self.EMAIL_INPUT).send_keys(email)
        # Вводим пароль
        self.driver.find_element(*self.PASSWORD_INPUT).send_keys(password)
        # Нажимаем кнопку "Войти"
        self.click(self.LOGIN_BTN)