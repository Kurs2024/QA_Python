from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

import time



driver = webdriver.Chrome()


def test_successful_reg(driver):
    driver.get('https://erikdark.github.io/zachet_selenium_01/register.html')
    login = driver.find_element(By.ID,'name').send_keys('Tatana')
    email = driver.find_element(By.ID,'email').send_keys('Tatana@mail.ru')
    password = driver.find_element(By.ID,'password').send_keys('Zxc123')
    btn = driver.find_element(By.CSS_SELECTOR,'button').click()
    time.sleep(5)
    message = driver.find_element(By.ID,'register-message').text
    assert message == 'Пользователь зарегистрирован'
time.sleep(5)


driver.quit()


