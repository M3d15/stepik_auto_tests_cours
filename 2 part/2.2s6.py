from selenium import webdriver
import time
import math
from math import log, sin

def calc(x):
    int_x = int(x)
    return log(abs(12*sin(int_x)))

try: 
    link = "http://SunInJuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # поиск первого значения
    find_x = browser.find_element_by_id("input_value")
    x = find_x.text
  
    # вычисление Х 
    res_x = calc(x)
    str_res = str(res_x)

    # поиск и заполнение поля ввода ответа
    find_answer = browser.find_element_by_id("answer")
    find_answer.send_keys(str_res)

    # скролл страницы на 150 пикселей вниз
    browser.execute_script("window.scrollBy(0, 150);")

    # поиск и выбор чекбокса "robotCheckbox"
    find_robotCheckbox = browser.find_element_by_id("robotCheckbox")
    # browser.execute_script("return arguments[0].scrollIntoView(true);", find_robotCheckbox)
    find_robotCheckbox.click()

    # поиск и выбор радио кнопки "robotsRule"
    find_robotsRule = browser.find_element_by_id("robotsRule").click()

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
