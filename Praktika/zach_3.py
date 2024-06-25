from selenium import webdriver
from selenium.webdriver.common.by import By
import time



driver = webdriver.Chrome()


def test_successful_reg(driver):
    driver.get('https://erikdark.github.io/zachet_selenium_01/profile.html')
    out_btn = driver.find_element(By.ID,'logout-button').click()
    
    message = driver.find_element(By.ID,'logout-message').text
    assert message == 'Пользователь вышел из системы'
    time.sleep(5)
    driver.quit()