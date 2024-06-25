from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest


@pytest.mark.login
def test_valid_login(driver):
    driver.get('https///')
    #.....(тест на логин валидный)
@pytest.mark.login
def test_invalid_login(driver):
    driver.get('https///')
    #.....(тест на логин  инвалидный)
@pytest.mark.dashboard
def test_dashboard(driver):
    driver.get('https///')
    #.....(тест на дашборд)
