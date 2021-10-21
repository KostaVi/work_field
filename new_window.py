from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)
    #button
    button = browser.find_element_by_xpath('//*[@type="submit"]')
    button.click()
    new_window=browser.window_handles[1]
    browser.switch_to.window(new_window)
    #alern
    #x=значение
    x_element = browser.find_element_by_id("input_value")
    x= x_element.text
    y=calc(x)
    #answer
    input2 = browser.find_element_by_id('answer')
    input2.send_keys (y)
    # Отправляем заполненную форму
    #submit
    button1= browser.find_element_by_xpath('//*[@type="submit"]')
    button1.click()

    time.sleep(1)
    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()