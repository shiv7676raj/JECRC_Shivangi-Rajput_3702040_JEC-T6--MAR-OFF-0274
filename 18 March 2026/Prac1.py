from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

from selenium.webdriver.common.keys import Keys

opts=webdriver.ChromeOptions()
opts.add_experimental_option("detach",True)
driver=webdriver.Chrome(options=opts)
#driver.get("https://www.lenskart.com/")
driver.get("https://www.lenskart.com/john-jacobs-jj-e10007-c11-full-rim-rectangle-eyeglasses.html")
driver.maximize_window()
sleep(2)
# eye=driver.find_element(By.ID,"lrd1")
# print(eye.text)
# assert 'GLASSES'==eye.text,"didn't find"
# assert 'EYEGLASSES'==eye.text,"didn't find"
pin=driver.find_element(By.XPATH,'//p[@title="Enter pincode"]')
#pin.send_keys("302017")
pin.click()
#sleep(2)
assert 'Enter pincode'==pin.text,"didn't find"
print('Success')
driver.quit()