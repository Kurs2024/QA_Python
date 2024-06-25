import pytest


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
driver = webdriver.Chrome()
def test_exection1():
    try:
       
        driver.get('https://erikdark.github.io/PyTest_01_reg_form/')


        element = driver.find_element(By.CSS_SELECTOR,'#username')
    finally:
        
        driver.quit()

   
               
    def test_exection():
        assert'hello'.upper()=='HELLO'
   
    
    






