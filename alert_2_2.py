from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)
    #button
    button = browser.find_element_by_xpath('//*[@type="submit"]')
    button.click()
    #alern
    confirm = browser.switch_to.alert
    confirm.accept()
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





    button = WebDriverWait(browser, 5).until(
        EC.element_to_be_clickable((By.ID, "verify")))
button.click()
message = browser.find_element_by_id("verify_message")

assert "successful" in message.text