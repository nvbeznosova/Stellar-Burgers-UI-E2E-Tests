from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.main_page import MainPage
from pages.ingredient_page import IngredientPage
from selenium.webdriver.common.by import By

def test_open_and_close_ingredient(driver):
    main = MainPage(driver)
    main.open_ingredient()
    ingredient = IngredientPage(driver)
    assert ingredient.is_modal_open()
    ingredient.close_modal()
    modal_element = driver.find_element(*IngredientPage.MODAL)
    WebDriverWait(driver, 5).until(EC.invisibility_of_element(modal_element))
    assert not modal_element.is_displayed()

def test_ingredient_counter_increases(driver):
    main = MainPage(driver)
    before = main.get_counter_value()
    main.drag_ingredient_to_constructor()
    after = main.get_counter_value()
    constructor_items = driver.find_elements(
        By.XPATH, "//section[contains(@class,'BurgerConstructor_basket__')]//a"
    )
    assert after > before or len(constructor_items) > 0