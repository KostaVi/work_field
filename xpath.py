from selenium import webdriver
import math
import time
z=(0)
#function
def calc(x,y):
  return (x+y)

try: 
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)
    x_element = browser.find_element_by_id("num1")
    x= (int(x_element.text))
    y_element = browser.find_element_by_id("num2")
    y= (int(y_element.text))
    z=calc(x,y)

    from selenium.webdriver.support.ui import Select
    select = Select(browser.find_element_by_css_selector("select#dropdown"))
    select.select_by_value(str(z)) # ищем элемент с текстом "Python"
    button = browser.find_element_by_css_selector('.btn-default').click()


    #dropdown







    time.sleep(1)
    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()