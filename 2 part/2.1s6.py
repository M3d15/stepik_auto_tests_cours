from selenium import webdriver
import time
import math

def calc(value_treasure):
  return str(math.log(abs(12*math.sin(int(value_treasure)))))

try: 
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)

    find_treasure = browser.find_element_by_id("treasure")
    value_treasure = find_treasure.get_attribute("valuex")
    y = calc(value_treasure)

    find_field_answer = browser.find_element_by_id("answer")
    find_field_answer.send_keys(y)

    find_checkbox1 = browser.find_element_by_id("robotCheckbox")
    find_checkbox1.click()

    find_radio1 = browser.find_element_by_id("robotsRule")
    find_radio1.click()

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
