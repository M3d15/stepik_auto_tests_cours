from selenium.common.exceptions import NoSuchElementException
from selenium import webdriver
import pytest
from selenium.webdriver.support.ui import WebDriverWait

def test_find_add_item_to_busket_button(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)
    browser.implicitly_wait(3)

    try:
        browser.find_element_by_css_selector("form#add_to_basket_form button.btn")

    except NoSuchElementException:
        assert False, "Button wasn't found"
    
