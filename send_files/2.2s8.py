from selenium import webdriver
import time
import os

try: 
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # поиск и заполнение первого поля
    input_first = browser.find_element_by_css_selector("input[name=firstname]:required")
    input_first.send_keys("Ivan")

    # поиск и заполнение второго поля
    input_second = browser.find_element_by_css_selector("input[name=lastname]:required")
    input_second.send_keys("Petrov")
  
    # поиск и заполнение третьего поля
    input_third = browser.find_element_by_css_selector("input[name=email]:required")
    input_third.send_keys("123@ya.ru")

    # поиск кнопки для загрузки файла
    find_download_button = browser.find_element_by_id("file")

    current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла 
    file_path = os.path.join(current_dir, 'file.txt')           # добавляем к этому пути имя файла 
    find_download_button.send_keys(file_path)

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
