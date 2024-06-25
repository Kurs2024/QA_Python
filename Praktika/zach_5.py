import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import re




#иницилизирую драйвер браузера
driver = webdriver.Chrome()


try:
    driver.get('https://erikdark.github.io/zachet_selenium_01/dynamic.html')
    time.sleep(1)

    driver.execute_script("document.getElementById('add-element').style.display='добавить элемент';")
    driver.find_element(By.CSS_SELECTOR,'#add-element').click()
    

    display_text = driver.find_element(By.CSS_SELECTOR,'content-area').text


    assert display_text == 'Элемент добавлен' 
   
   




finally:
    time.sleep(5)
    driver.quit()

    

   


