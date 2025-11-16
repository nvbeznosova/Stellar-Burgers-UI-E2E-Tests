import pytest
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.order_feed_page import OrderFeedPage

def test_order_form(driver):
    login = LoginPage(driver)
    login.login("testuser@example.com", "password123")

    feed = OrderFeedPage(driver)
    total_before = feed.get_total_count()
    today_before = feed.get_today_count()

    main = MainPage(driver)
    main.drag_ingredient_to_constructor()

    main.click_order_button()
    assert main.is_order_modal_open()

    modal_text = main.get_text(MainPage.ORDER_MODAL)
    assert "Ваш заказ начали готовить" in modal_text

    total_after = feed.get_total_count()
    today_after = feed.get_today_count()
    assert total_after > total_before
    assert today_after > today_before

    assert str(total_after) in feed.get_in_progress_orders()