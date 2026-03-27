from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep

driver=webdriver.Chrome()
driver.get("https://codepen.io/gdw96/pen/jOypoYL")
driver.maximize_window()
i_frame=driver.find_element(By.TAG_NAME,"iframe")
driver.switch_to.frame(i_frame)
username=driver.find_element(By.ID,"username")
username.send_keys("name")
password=driver.find_element(By.ID,"password")
password.send_keys("pass")
eye=driver.find_element(By.CLASS_NAME,"fa-eye")
actions=ActionChains(driver)
actions.click_and_hold(eye).perform()
sleep(2)
actions.release().perform()
register=driver.find_element(By.XPATH,"//input[@class='submit']")
register.click()
sleep(5)
driver.back()
i_frame=driver.find_element(By.TAG_NAME,"iframe")
driver.switch_to.frame(i_frame)
heading=driver.find_element(By.XPATH,"//h1")
assert "Registration" in heading.text
print("Success!!")
sleep(2)
driver.quit()