from selenium import webdriver

browser = webdriver.Chrome()
link = "http://suninjuly.github.io/cats.html"
browser.get(link)
button = browser.find_element_by_id("button")
button.click()