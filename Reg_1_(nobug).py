from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os
# указывая директорию,где лежит файлу.txt
# в конце должен быть /
directory = "C:/"

# имя файла, который будем загружать на сайт
file_name = "test_sel.txt"

# собираем путь к файлу
file_path=os.path.join(directory,file_name)
# отправляем файл


try: 
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)
    # Отправляем заполненную форму
    input1 = browser.find_element_by_css_selector('[name="firstname"]')
    input1.send_keys("Ivan")
    input2 = browser.find_element_by_css_selector('[name="lastname"]')
    input2.send_keys("Petrov")
    input3 = browser.find_element_by_css_selector('[name="email"]')
    input3.send_keys("IP23")
    #directory
    element_1=browser.find_element_by_css_selector('[type="file"]')
    element_1.send_keys(file_path)

    button = browser.find_element_by_xpath('//*[@type="submit"]')
    button.click()
    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element_by_tag_name("h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(3)
    # закрываем браузер после всех манипуляций
    browser.quit()