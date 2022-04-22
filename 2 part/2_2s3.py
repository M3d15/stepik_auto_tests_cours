from selenium import webdriver
import time
import math
from selenium.webdriver.support.ui import Select

def calc(first_number, second_number):
    return int(first_number) + int(second_number)

try: 
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # поиск первого значения
    find_first_number = browser.find_element_by_id("num1")
    first_number = find_first_number.text

    # поиск второго значения
    find_second_number = browser.find_element_by_id("num2")
    second_number = find_second_number.text

    # сложение двух значений
    sum = calc(first_number, second_number)
    sum_str = str(sum)   

    select = Select(browser.find_element_by_css_selector("select#dropdown.custom-select"))
    select.select_by_value(sum_str) # ищем элемент с текстом равный сумме двех значений

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
