
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver = webdriver.Chrome()

driver.get('http://selenium1py.pythonanywhere.com/ru/')








book1 = driver.find_element(By.CSS_SELECTOR, 'cache/44/0a/440a00e71baf4e0f3c5092d6f1973d63.jpg')
button_type1=driver.find_element(By.CSS_SELECTOR, 'btn btn-lg btn-primary btn-add-to-basket')
button_type1.click()

book2 = driver.fbind_element(By.CSS_SELECTOR, 'cache/16/06/1606caaad729534bb27f883340eff941.jpg').click()
button_type2=driver.find_element(By.CSS_SELECTOR, 'btn btn-lg btn-primary btn-add-to-basket').click()

book3 = driver.fbind_element(By.CSS_SELECTOR, 'cache/a4/65/a465de9eafadb606e63901afbf1e540b.jpg').click()
button_type3=driver.find_element(By.CSS_SELECTOR, 'btn btn-lg btn-primary btn-add-to-basket').click()

book4 = driver.fbind_element(By.CSS_SELECTOR, 'cache/a4/65/a465de9eafadb606e63901afbf1e540b.jpg').click()
button_type4=driver.find_element(By.CSS_SELECTOR, 'btn btn-lg btn-primary btn-add-to-basket').click()

assert'da'








   





 







if __name__ == "__main__":
   pytest.main()