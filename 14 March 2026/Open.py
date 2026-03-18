from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://testautomationpractice.blogspot.com/")
sleep(3)
# driver.get("https://www.cricbuzz.com/")
# sleep(3)
# driver.get("https://www.myntra.com/")
# sleep(3)
#use ctrl+f to find these in inspect of sites
# a=driver.find_element(By.XPATH,'//span[text()="All"]/ancestor::div[@id="nav-main"]')
# print(a)
# b=driver.find_element(By.XPATH,'//div[@id="nav-main"]/descendant::span[text()="All"]')
# print(b)
#following-sibling and preceding-sibling
#//a[text()="Fresh"]/ancestor::ul/following-sibling::li[1]]
# k=driver.find_element(By.LINK_TEXT,"Udemy Courses")
# print("found the element using link text")
# d=driver.find_element(By.PARTIAL_LINK_TEXT,"Udemy")
# print('found the element using partial-link text')
# a=driver.find_element(By.XPATH,'//td[text()="Learn Java"]/following-sibling::td[3]')
# print(a)
#operations on table
#//td[text()="Amod"]/following-sibling::td[3]
#//td[text()="Amod"]/ancestor::tr[1]/preceding-sibling::tr[4]/td
e=driver.find_elements(By.XPATH,'//td[text()="300"]/preceding-sibling::td[3]')
print(len(e))
for i in e:
    print(i.text)
names = driver.find_elements(By.XPATH, "//table//tr/td[1]")
for n in names:
    print(n.text)
print('found the elements')