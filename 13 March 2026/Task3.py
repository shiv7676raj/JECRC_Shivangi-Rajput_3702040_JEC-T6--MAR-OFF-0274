from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
driver = webdriver.Chrome()
driver.get("https://www.amazon.in/")
driver.maximize_window()
sleep(5)
search_bar = driver.find_element(By.CSS_SELECTOR,"#twotabsearchtextbox")
print(search_bar)
logo = driver.find_element(By.CSS_SELECTOR,"#nav-logo-sprites")
print(logo)
cart = driver.find_element(By.CSS_SELECTOR,"#nav-cart")
print(cart)
signin = driver.find_element(By.CSS_SELECTOR,"#nav-tools a")
print(signin)
categories = driver.find_elements(By.CSS_SELECTOR,"#nav-xshop a")
print(categories)
print("Total categories found:",len(categories))
driver.quit()