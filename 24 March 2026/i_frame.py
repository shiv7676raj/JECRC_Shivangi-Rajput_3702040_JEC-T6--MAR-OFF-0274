from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome()
driver.get("https://demo.automationtesting.in/Frames.html")
driver.maximize_window()
sleep(2)
# iframe=driver.find_element(By.ID,"singleframe")
# driver.switch_to.frame(iframe)
# sleep(2)
# driver.find_element(By.XPATH,'//input[@type="text"]').send_keys("Helooooo")
# sleep(3)

#nested iframes
driver.find_element(By.XPATH,'//a[text()="Iframe with in an Iframe"]').click()
nested=driver.find_element(By.XPATH,'//iframe[@src="MultipleFrames.html"]')
driver.switch_to.frame(nested)

inner=driver.find_element(By.XPATH,'//iframe[@src="SingleFrame.html"]')
driver.switch_to.frame(inner)

driver.find_element(By.XPATH,'//input[@type="text"]').send_keys("Helooooo")
sleep(2)

driver.switch_to.parent_frame()     #switches to parent frame
driver.switch_to.default_content()  #switches to default page

