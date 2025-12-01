from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.order_feed_page import OrderFeedPage

def test_order_form(driver):
    login = LoginPage(driver)
    login.open_login_form()
    login.login("fedya@yandex.ru", "Fedya2025")

    WebDriverWait(driver, 30).until(
        EC.visibility_of_element_located(MainPage.CONSTRUCTOR_AREA)
    )

    main = MainPage(driver)
    main.go_to_order_feed()

    feed = OrderFeedPage(driver)
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(OrderFeedPage.TOTAL_COUNTER)
    )
    total_before = feed.get_total_count()
    today_before = feed.get_today_count()

    main.go_to_constructor()
    main.drag_ingredient_to_constructor()
    main.click_order_button()

    WebDriverWait(driver, 45).until(
        EC.visibility_of_element_located(MainPage.ORDER_MODAL)
    )
    assert main.is_order_modal_open()

    modal_text = main.get_text(MainPage.ORDER_MODAL).lower()
    assert "заказ" in modal_text

    main.go_to_order_feed()
    WebDriverWait(driver, 45).until(lambda d: feed.get_total_count() >= total_before)
    WebDriverWait(driver, 45).until(lambda d: feed.get_today_count() >= today_before)

    total_after = feed.get_total_count()
    today_after = feed.get_today_count()

    assert total_after >= total_before
    assert today_after >= today_before

    in_progress_after = feed.get_in_progress_orders()
    assert len(in_progress_after) > 0
