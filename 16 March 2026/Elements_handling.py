from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
opts=webdriver.ChromeOptions()
opts.add_experimental_option('detach',True)
driver=webdriver.Chrome(options=opts)
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()
# name=driver.find_element(By.ID,'name')
# name.clear()
# name.send_keys('Shivangi')
# print(name.get_attribute('placeholder'))
# print(name.get_attribute('value'))
# sleep(2)
# email=driver.find_element(By.XPATH,'//input[@placeholder="Enter EMail"]')
# email.send_keys('shiv@gmail.com')
# genders=driver.find_elements(By.XPATH,"//input[@name='gender']")
# for i in genders:
#     i.click()
#     sleep(2)

# box=driver.find_elements(By.XPATH,"//input[@type='checkbox']")[:7]
# for i in box:
#     i.click()
#     days = i.find_element(By.XPATH, "following-sibling::label").text
#     print(days)
#     sleep(1)
# for i in box[::-1]:
#     i.click()
#     sleep(1)

# driver.get("https://www.flipkart.com/")
# driver.maximize_window()
# sleep(2)
# s=driver.find_element(By.NAME,"q")
# s.send_keys("laptops")
# driver.find_element(By.XPATH,"//button[@type='submit']").click()
# sleep(1)
# box=driver.find_elements(By.XPATH,"//input[@type='checkbox']")
# for i in box:
#     i.click()
#     n=i.find_element(By.XPATH,"following-sibling::div").text
#     print(n)
#     sleep(1)

male=driver.find_element(By.ID,"male")
male.click()
print(male.is_displayed())
print(male.is_enabled())
check=driver.find_element(By.XPATH,"//label[text()='Monday']/preceding-sibling::input")
check.click()
print(check.is_selected())
m=driver.find_element(By.XPATH,'//input[@id="monday"]/following-sibling::label')
print(m.text)
sleep(2)

# driver.get("https://www.amazon.in/")
# driver.maximize_window()
# sleep(3)
# search_f=driver.find_element(By.ID,'twotabsearchtextbox')
# print(search_f.get_attribute('placeholder'))
# print(search_f.get_attribute('value'))
# search_f.clear()
# search_f.send_keys('Mobile Phones',Keys.ENTER)
# button=driver.find_element(By.ID,'nav-search-submit-button')
# button.click()
# sleep(3)
# driver.quit()
driver.quit()