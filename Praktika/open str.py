
import time
#импортирую сам вебдрайвер
from selenium import webdriver
#импортирую класс By который ищет элемент на странице
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import re




#иницилизирую драйвер браузера
driver = webdriver.Chrome()




try:
    driver.get('https://erikdark.github.io/QA_autotests_12/')
    time.sleep(1)


    driver.find_element(By.CSS_SELECTOR,'#startTaskBtn').click()
    driver.switch_to.alert.accept()
    driver.switch_to.alert.send_keys('50')
    driver.switch_to.alert.accept()
    a = driver.switch_to.alert.text
    assert 'Правильно! Ответ 50.' == a
   




finally:
    time.sleep(5)
    driver.quit()


