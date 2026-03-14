from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/login")
driver.maximize_window()
sleep(3)
username = driver.find_element(By.XPATH, "//input[@name='username']")
print(username)
password = driver.find_element(By.XPATH, "//input[@id='password']")
print(password)
login_btn = driver.find_element(By.XPATH, "//button[@type='submit']")
print(login_btn)
elemental_link = driver.find_element(By.XPATH, "//a[text()='Elemental Selenium']")
print(elemental_link)
heading = driver.find_element(By.XPATH, "//h2[contains(text(),'Login')]")
print(heading)
print("All elements located successfully")
#driver.quit()