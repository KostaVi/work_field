from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import math
import time
#function
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "http://SunInJuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)
    x_element = browser.find_element_by_id("input_value")
    x= x_element.text
    y=calc(x)
    # Отправляем заполненную форму
    input2 = browser.find_element_by_id('answer')
    input2.send_keys (y)

    #check
    option2 = browser.find_element_by_id("robotCheckbox")
    option2.click()
    #radio
    option1 = browser.find_element_by_id("robotsRule")
    browser.execute_script("return arguments[0].scrollIntoView(true);",option1)
    option1.click()


    # button
    button = browser.find_element_by_xpath('//*[@type="submit"]')
    browser.execute_script("return arguments[0].scrollIntoView(true);",button)
    button.click()

    
    time.sleep(1)
    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()