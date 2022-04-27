from selenium import webdriver
from selenium.webdriver.common.by import By
import selenium.webdriver.support.expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time
import math
import pytest

def answer():
    return math.log(int(time.time()))

@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()

@pytest.mark.parametrize('domain', ["236895", "236896", "236897", "236898", "236899", "236903", "236904", "236905"])
def test_guest_should_see_login_link(browser, domain):
    link = f"https://stepik.org/lesson/{domain}/step/1"
    browser.get(link)
    #browser.implicitly_wait(5)

    WebDriverWait(browser, 5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'textarea.ember-text-area'))
        ).send_keys(str(answer()))

    #find_input = browser.find_element_by_css_selector("textarea.ember-text-area")
    #find_input.send_keys(str(answer()))

    browser.find_element_by_css_selector("button.submit-submission").click()

    #browser.implicitly_wait(5)

    find_text = WebDriverWait(browser, 5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '.smart-hints__hint'))
        ).text

    #find_notice = browser.find_element_by_css_selector(".smart-hints__hint")
    #find_text = find_notice.text

    assert find_text == "Correct!", "Notice is incorrect!"
