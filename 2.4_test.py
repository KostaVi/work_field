from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome()
    browser.get(link)
    #button_book
    button= WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, "price"),"$100"))
    button1= browser.find_element_by_id('book')
    button1.click()
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
    button2= browser.find_element_by_xpath('//*[@type="submit"]')
    button2.click()
    #time
    time.sleep(1)
    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()


    print(x)