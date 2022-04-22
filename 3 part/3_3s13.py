from selenium import webdriver
import time
import unittest

class TestReg(unittest.TestCase):
    def test_reg1(self):
    	link = "http://suninjuly.github.io/registration1.html"
    	browser = webdriver.Chrome()
    	browser.get(link)

   	# Поиск полей ввода и заполнения их, значениями
    	input1 = browser.find_element_by_css_selector('div.first_block input.form-control.first:required')
    	input1.send_keys("Ivan")

    	input2 = browser.find_element_by_css_selector('div.first_block input.form-control.second:required')
    	input2.send_keys("Petrov")

    	input3 = browser.find_element_by_css_selector('div.first_block input.form-control.third:required')
    	input3.send_keys("123@ya.ru")

   	# Отправляем заполненную форму
    	button = browser.find_element_by_css_selector("button.btn")
    	button.click()

    	# Проверяем, что смогли зарегистрироваться
    	# ждем загрузки страницы
    	time.sleep(1)

    	# находим элемент, содержащий текст
    	welcome_text_elt = browser.find_element_by_tag_name("h1")
  	# записываем в переменную welcome_text текст из элемента welcome_text_elt
    	welcome_text = welcome_text_elt.text

    	# с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    	self.assertEqual("Congratulations! You have successfully registered!", welcome_text, "reg1 failed")

   	# закрываем браузер после всех манипуляций
    	browser.quit()

    def test_reg2(self):
    	link = "http://suninjuly.github.io/registration2.html"
    	browser = webdriver.Chrome()
    	browser.get(link)

   	# Поиск полей ввода и заполнения их, значениями
    	input1 = browser.find_element_by_css_selector('div.first_block input.form-control.first:required')
    	input1.send_keys("Ivan")

    	input2 = browser.find_element_by_css_selector('div.first_block input.form-control.second:required')
    	input2.send_keys("Petrov")

    	input3 = browser.find_element_by_css_selector('div.first_block input.form-control.third:required')
    	input3.send_keys("123@ya.ru")

   	# Отправляем заполненную форму
    	button = browser.find_element_by_css_selector("button.btn")
    	button.click()

    	# Проверяем, что смогли зарегистрироваться
    	# ждем загрузки страницы
    	time.sleep(1)

    	# находим элемент, содержащий текст
    	welcome_text_elt = browser.find_element_by_tag_name("h1")
  	# записываем в переменную welcome_text текст из элемента welcome_text_elt
    	welcome_text = welcome_text_elt.text

    	# с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    	self.assertEqual("Congratulations! You have successfully registered!", welcome_text, "reg2 failed")

   	# закрываем браузер после всех манипуляций
    	browser.quit()

if __name__ == "__main__":
    unittest.main()