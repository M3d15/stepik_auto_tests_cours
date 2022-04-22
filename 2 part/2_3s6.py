from selenium import webdriver
import time
import math
from math import log, sin

def calc(x):
    int_x = int(x)
    return log(abs(12*sin(int_x)))

try: 
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    find_first_button = browser.find_element_by_css_selector(".trollface.btn").click()

    second_window = browser.window_handles[1]
    browser.switch_to.window(second_window)
  
    # поиск Х 
    find_x = browser.find_element_by_id("input_value")
    x = find_x.text 
    
    # вычисление Х и преобразование результата в строку
    res_x = calc(x)
    str_res = str(res_x)

    # поиск и заполнение поля ввода ответа
    find_answer = browser.find_element_by_id("answer")
    find_answer.send_keys(str_res)

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
