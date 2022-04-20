from selenium import webdriver
import time
import math
from math import log, sin

def calc(x):
    int_x = int(x)
    return log(abs(12*sin(int_x)))

try: 
    link = "http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # поиск первого значения
    find_first_button = browser.find_element_by_class_name("btn").click()

    # переключение на модальное окно и принятие сообщения
    confirm = browser.switch_to.alert.accept()
  
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
