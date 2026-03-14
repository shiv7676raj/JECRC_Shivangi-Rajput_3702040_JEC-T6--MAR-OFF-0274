from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By

opts=webdriver.ChromeOptions()
opts.add_experimental_option('detach', True)
driver=webdriver.Chrome(options=opts)
driver.get('https://demoqa.com/automation-practice-form')
driver.maximize_window()
sleep(4)
name=driver.find_element(By.ID,'firstName')  #NoSuchElementFound exception if id nt found
email=driver.find_element(By.ID,'userEmail')
radio_button=driver.find_elements(By.CLASS_NAME,'form-check-input')
print(radio_button)
inp=driver.find_elements(By.TAG_NAME,'textarea')
print(len(inp))
print('Everything found')
driver.quit()