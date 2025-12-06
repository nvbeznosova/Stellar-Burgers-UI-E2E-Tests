import allure
from pages.main_page import MainPage
from pages.ingredient_page import IngredientPage

@allure.suite("Ингредиенты")
class TestIngredient:

    @allure.title("Открытие модального окна ингредиента по клику")
    def test_open_ingredient_modal(self, driver):
        main = MainPage(driver)
        main.open_ingredient()
        ingredient = IngredientPage(driver)
        assert ingredient.is_modal_open()

    @allure.title("Закрытие модального окна ингредиента по крестику")
    def test_close_ingredient_modal(self, driver):
        main = MainPage(driver)
        main.open_ingredient()
        ingredient = IngredientPage(driver)
        assert ingredient.is_modal_open()
        ingredient.close_modal()
        assert ingredient.wait_invisible(IngredientPage.MODAL)

    @allure.title("При добавлении ингредиента в заказ счётчик увеличивается")
    def test_ingredient_counter_increases(self, driver):
        main = MainPage(driver)
        before = main.get_counter_value()
        main.drag_ingredient_to_constructor()
        after = main.get_counter_value()
        assert after >= before