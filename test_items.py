import time
from selenium.webdriver.common.by import By

def test_button_availability(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)

    browser.implicitly_wait(10)

    assert browser.find_element(By.CSS_SELECTOR, ".btn-add-to-basket").is_displayed()
