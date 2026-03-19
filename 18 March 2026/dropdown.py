from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from time import sleep

# driver=webdriver.Chrome()
# driver.get("https://testautomationpractice.blogspot.com/")
# driver.maximize_window()
# dd=driver.find_element(By.ID,"country")
# dropdown=Select(dd)
# dropdown.select_by_value("uk")
# sleep(4)
# dropdown.select_by_index(4)
# sleep(2)
# dropdown.select_by_visible_text('Japan')
# sleep(2)

driver=webdriver.Chrome()
driver.get("https://www.lenskart.com/")
driver.maximize_window()
driver.find_element(By.ID,"lrd1").click()
sleep(2)
dd=driver.find_element(By.ID,"sortByDropdown")
dropdown=Select(dd)
dropdown.select_by_value("low_price")
sleep(3)
first = driver.find_element(By.XPATH,'//div[@class="sc-bf32d8a7-0 gOVKHN"]/descendant::div/p')
print(first.text)
driver.quit()