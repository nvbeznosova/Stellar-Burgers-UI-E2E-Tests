from pages.main_page import MainPage

def test_go_to_constructor(driver):
    page = MainPage(driver)
    page.go_to_constructor()
    assert page.is_visible(MainPage.CONSTRUCTOR_AREA)

def test_go_to_order_feed(driver):
    page = MainPage(driver)
    page.go_to_order_feed()
    assert page.is_visible(MainPage.ORDER_FEED_LINK)
