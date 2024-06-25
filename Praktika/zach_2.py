from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver=webdriver.Chrome()
driver.get('https://erikdark.github.io/zachet_selenium_01/login.html')
mail_name=driver.find_element(By.ID,'email').send_keys('Tatana@mail.ru')
password=driver.find_element(By.ID,'password').send_keys('Zxc123')
btn=driver.find_element(By.CSS_SELECTOR,'button[type="submit"]')
btn.click()
time.sleep(5)
