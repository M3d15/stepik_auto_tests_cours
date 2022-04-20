from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math
import time
from math import log, sin

def calc(x):
    int_x = int(x)
    return log(abs(12*sin(int_x)))

try: 
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # говорим Selenium проверять в течение 12 секунд, пока кнопка не станет кликабельной
    WebDriverWait(browser, 12).until(
	EC.text_to_be_present_in_element((By.ID, "price"), "100"))
    
    browser.find_element_by_id("book").click()
  
    # поиск Х 
    find_x = browser.find_element_by_id("input_value")
    x = find_x.text 
    
    # вычисление Х и преобразование результата в строку
    res_x = calc(x)
    str_res = str(res_x)

    # поиск и заполнение поля ввода ответа
    find_answer = browser.find_element_by_id("answer")
    find_answer.send_keys(str_res)

    # скролл вниз к полю ввода ответа
    browser.execute_script("return arguments[0].scrollIntoView(true);", find_answer)
  
    # Отправляем заполненную форму
    button = browser.find_element_by_id("solve")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
