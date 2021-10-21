from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import random
#value
link = "https://klientiks.ru/login"
phone_number =(9627065473)
passw=(153290)
n_count= int(0)
a=0
b=1
user= ('User_')
#functions
#def_random
def date_random(date_day,date_month,date_year):
    return (str(date_day) + str(date_month) + str(date_year))
#steam
try: 
#connect
    browser = webdriver.Chrome()
    browser.implicitly_wait(451)
    browser.get(link)
#authorization
       #login
    input_phone = browser.find_element_by_css_selector('.element_cr #label-phone')
    input_phone.send_keys (phone_number)
       #password
    input_passw = browser.find_element_by_css_selector('#label-password')
    input_passw.send_keys (passw)
#button_enter_login
    button_enter = browser.find_element_by_css_selector('.element-button_button')
    button_enter.click()
    time.sleep(30)
#button_clients
    button_clients = browser.find_element_by_css_selector('#body > div.t-header > div.b-header > div:nth-child(5) > a')
    button_clients.click()
    #new_window
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)
    #add_client
    #way_1
    button_add_clients_first = browser.find_element_by_css_selector('#breadCrumbs > div.b-bread_crumb._first.jsBreadFirst > div.b-bread_buttons > div > span')
    button_add_clients_first.click()
    #cicle
    while n_count <50:
        n_count=n_count+1
        user_input=(user+(str(n_count)))
        #def_fibonacci
        a,b=b,a+b
        #random_value
        date_day=random.randrange(1,30,1)
        if len(str(date_day))==1:
            date_day= (str(0)+str(date_day))
        date_month=random.randrange(1,12,1)
        if len(str(date_month))==1:
            date_month= (str(0)+str(date_month))
        date_year=random.randrange(1970,2000,1)
        date_input=date_random(date_day,date_month,date_year)
        #add_client
        button_add_clients = browser.find_element_by_css_selector('#breadCrumbs > div.b-bread_crumb._first.jsBreadFirst > div.b-bread_buttons > div')
        button_add_clients.click()
        time.sleep(2)
        #add_name
        input_name = browser.find_element_by_css_selector('input#label-first_name')
        input_name.send_keys (user_input)
        #add_id
        input_id_clear = browser.find_element_by_id('label-number').clear()
        time.sleep(2)
        input_id = browser.find_element_by_id('label-number')
        input_id.send_keys (b)
        #add_date
        input_date = browser.find_element_by_id('label-birth_date')
        input_date.send_keys (date_input)
        #checkbox
        button_check = browser.find_element_by_xpath('/html/body/div[3]/div[2]/div/div/div[2]/div/div[2]/form/div[8]/div[2]/div[2]/label')
        button_check.click()
        #save
        button_save = browser.find_element_by_css_selector('.jsSaveButtonCreate .b-bread_button_span')
        button_save.click()
        time.sleep(2)
finally:

    assert "successful"