from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage

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

    def go_to_constructor(self):
        self._safe_click(self.CONSTRUCTOR_LINK)

    def go_to_order_feed(self):
        if self.is_element_present(self.ORDER_MODAL):
            self._safe_click(self.ORDER_MODAL_CLOSE)
            WebDriverWait(self.driver, 10).until(EC.invisibility_of_element_located(self.ORDER_MODAL))
        self._safe_click(self.ORDER_FEED_LINK)

    def _safe_click(self, locator):
        elem = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(locator))
        self.driver.execute_script("arguments[0].scrollIntoView({block:'center'});", elem)
        try:
            elem.click()
        except Exception:
            self.driver.execute_script("arguments[0].click();", elem)

    def open_ingredient(self):
        self.click(self.INGREDIENT)

    def get_counter_value(self):
        return int(self.get_text(self.INGREDIENT_COUNTER))

    def drag_ingredient_to_constructor(self):
        ingredient = self.driver.find_element(*self.INGREDIENT)
        target = self.driver.find_element(*self.CONSTRUCTOR_AREA)
        self.driver.execute_script("""
            function triggerDragAndDrop(sourceNode, destinationNode) {
                var event = document.createEvent('CustomEvent');
                event.initCustomEvent('dragstart', true, true, null);
                sourceNode.dispatchEvent(event);

                event = document.createEvent('CustomEvent');
                event.initCustomEvent('drop', true, true, null);
                destinationNode.dispatchEvent(event);

                event = document.createEvent('CustomEvent');
                event.initCustomEvent('dragend', true, true, null);
                sourceNode.dispatchEvent(event);
            }
            triggerDragAndDrop(arguments[0], arguments[1]);
        """, ingredient, target)

    def click_order_button(self):
        self.click(self.ORDER_BTN)

    def is_order_modal_open(self):
        return self.is_visible(self.ORDER_MODAL)

    def get_order_number(self):
        return self.get_text((By.XPATH, "//section[contains(@class,'Modal_modal_opened__')]//h2"))