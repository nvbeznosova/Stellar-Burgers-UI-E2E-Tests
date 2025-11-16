from pages.main_page import MainPage

def test_go_to_constructor(driver):
    page = MainPage(driver)
    page.go_to_constructor()
    assert "constructor" in driver.current_url

def test_go_to_order_feed(driver):
    page = MainPage(driver)
    page.go_to_order_feed()
    assert "feed" in driver.current_url