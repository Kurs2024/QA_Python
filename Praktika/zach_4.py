
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

import time
driver = webdriver.Chrome()


def filter(driver):

    driver.get('https://erikdark.github.io/zachet_selenium_01/table.html')
    table=driver.find_element(By.ID,'data-table')
    rows=table.find_elements(By.TAG_NAME,'tr')
    fist_col=[row.find_elements(By.TAG_NAME,'td')[0].text for row in rows[1:]]
    
    st_1=driver.find_element(By.CSS_SELECTOR,'sortTable(0)').click()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
time.sleep(5)   
 
driver.quit()
