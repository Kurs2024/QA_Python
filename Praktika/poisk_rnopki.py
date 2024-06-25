import time
#импортирую сам вебдрайвер
from selenium import webdriver
#импортирую класс By который ищет элемент на странице
from selenium.webdriver.common.by import By


#иницилизирую драйвер браузера
driver = webdriver.Chrome()
driver.get('https://erikdark.github.io/Qa_autotest_02/')
btns = driver.find_elements(By.CSS_SELECTOR, '.btn')
time.sleep(1)
btns.send_keys('phone','email','name','password')
time.sleep(5)
