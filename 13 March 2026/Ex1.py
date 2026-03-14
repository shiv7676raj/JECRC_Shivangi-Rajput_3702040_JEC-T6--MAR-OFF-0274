from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By

opts=webdriver.ChromeOptions()
opts.add_experimental_option('detach', True)
driver=webdriver.Chrome(options=opts)
driver.get('https://testautomationpractice.blogspot.com/')
driver.maximize_window()
sleep(4)
# # name=driver.find_element(By.ID,'name')  #NoSuchElementFound exception if id nt found
# # PNo=driver.find_element(By.ID,'phone')
# # nav_bar=driver.find_element(By.NAME,'Navbar')
# # radio_button=driver.find_elements(By.CLASS_NAME,'foreck-input')
# # print(radio_button)
# # inp=driver.find_elements(By.TAG_NAME,'input')
# # print(len(inp))
# name=driver.find_element(By.CSS_SELECTOR,'select[id="animals"]')
# ani=driver.find_element(By.CSS_SELECTOR,'#animals')
# #<a href="http://testautomationpractice.blogspot.com/">Home</a>
# #  finds the first occurrence of link
# an=driver.find_element(By.CSS_SELECTOR,'a[href*="testautomationpractice"]')   #partial link/substring
# print('a',an)
# an1=driver.find_element(By.CSS_SELECTOR,'a[href^="https://"]')  #to start with http
# print('a',an1)
# an2=driver.find_element(By.CSS_SELECTOR,'a[href$=".com"]')    #to end with .com
# print('a',an2)
# print('Everything found')
# driver.quit()
#XPath-xml
#/html-absolute xpath(/body/div/input[@ id='name'])
#//html-relative xpath(//input[@ id='name'])
# x=driver.find_element(By.XPATH,'//input[@placeholder="Enter Name"]')
# print(x)
# y=driver.find_element(By.XPATH,'(//input[@class="form-control"])[1]')
# print(y)
#to get inner text present in tags-//a[text()="Home"]
aa=driver.find_element(By.XPATH,'//a[text()="Home"]')
print(aa)
#use contains to avoid error below which works like identity operator 'in'
bb=driver.find_element(By.XPATH,'//h1[contains(text(),"Automation Testing Practice")]')
print(bb)
