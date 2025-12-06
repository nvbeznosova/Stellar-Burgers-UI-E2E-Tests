from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
import allure

class BasePage:
    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    @allure.step("Клик по элементу")
    def click(self, locator):
        elem = self.wait.until(EC.element_to_be_clickable(locator))
        elem.click()

    @allure.step("JS-клик по элементу")
    def js_click(self, locator):
        elem = self.wait.until(EC.element_to_be_clickable(locator))
        self.driver.execute_script("arguments[0].click();", elem)

    @allure.step("Прокрутка к элементу")
    def scroll_into_view(self, locator):
        elem = self.wait.until(EC.visibility_of_element_located(locator))
        self.driver.execute_script("arguments[0].scrollIntoView({block:'center'});", elem)

    @allure.step("Безопасный клик (скролл + fallback)")
    def safe_click(self, locator):
        elem = self.wait.until(EC.element_to_be_clickable(locator))
        self.driver.execute_script("arguments[0].scrollIntoView({block:'center'});", elem)
        try:
            elem.click()
        except Exception:
            self.driver.execute_script("arguments[0].click();", elem)

    @allure.step("Получение текста элемента")
    def get_text(self, locator):
        elem = self.wait.until(EC.visibility_of_element_located(locator))
        return elem.text

    @allure.step("Проверка видимости элемента")
    def is_visible(self, locator):
        try:
            self.wait.until(EC.visibility_of_element_located(locator))
            return True
        except Exception:
            return False

    @allure.step("Ожидание невидимости элемента")
    def wait_invisible(self, locator):
        return self.wait.until(EC.invisibility_of_element_located(locator))

    @allure.step("Поиск элемента")
    def find(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))

    @allure.step("Поиск элементов")
    def find_all(self, locator):
        self.wait.until(EC.presence_of_all_elements_located(locator))
        return self.driver.find_elements(*locator)

    @allure.step("Ввод текста")
    def type_text(self, locator, text):
        elem = self.wait.until(EC.visibility_of_element_located(locator))
        elem.clear()
        elem.send_keys(text)

    @allure.step("Drag-and-drop через ActionChains с JS fallback")
    def drag_and_drop(self, source_locator, target_locator):
        source = self.wait.until(EC.visibility_of_element_located(source_locator))
        target = self.wait.until(EC.visibility_of_element_located(target_locator))
        try:
            ActionChains(self.driver).drag_and_drop(source, target).perform()
        except Exception:
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
            """, source, target)