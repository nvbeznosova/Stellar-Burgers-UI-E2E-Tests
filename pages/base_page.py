from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def click(self, locator):
        """Дождаться кликабельности и кликнуть по элементу"""
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    def get_text(self, locator):
        """Дождаться видимости и вернуть текст элемента"""
        return self.wait.until(EC.visibility_of_element_located(locator)).text

    def is_visible(self, locator):
        """Проверить, виден ли элемент"""
        try:
            return self.wait.until(EC.visibility_of_element_located(locator))
        except:
            return False

    def is_element_present(self, locator):
        """Проверить, есть ли элемент в DOM (без ожидания видимости)"""
        try:
            self.driver.find_element(*locator)
            return True
        except:
            return False

    def type_text(self, locator, text):
        """Очистить поле и ввести текст"""
        elem = self.wait.until(EC.visibility_of_element_located(locator))
        elem.clear()
        elem.send_keys(text)

    def drag_and_drop(self, source, target):
        """Перетащить элемент source в target через JavaScript"""
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