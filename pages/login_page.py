from selenium.webdriver.common.by import By
from pages.base_page import BasePage
import allure

class LoginPage(BasePage):
    LOGIN_ACCOUNT_BTN = (By.XPATH, "//button[text()='Войти в аккаунт']")
    EMAIL_INPUT = (By.NAME, "name")
    PASSWORD_INPUT = (By.NAME, "Пароль")
    LOGIN_BTN = (By.XPATH, "//button[text()='Войти']")

    @allure.step("Открываем форму логина")
    def open_login_form(self):
        self.safe_click(self.LOGIN_ACCOUNT_BTN)

    @allure.step("Авторизуемся с email и паролем")
    def login(self, email, password):
        self.type_text(self.EMAIL_INPUT, email)
        self.type_text(self.PASSWORD_INPUT, password)
        self.click(self.LOGIN_BTN)