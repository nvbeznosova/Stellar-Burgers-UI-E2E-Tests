from pages.main_page import MainPage
from pages.ingredient_page import IngredientPage

def test_open_and_close_ingredient(driver):
    main = MainPage(driver)
    main.open_ingredient()
    ingredient = IngredientPage(driver)
    assert ingredient.is_modal_open()
    ingredient.close_modal()