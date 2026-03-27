from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver=webdriver.Chrome()
driver.get("https://demoqa.com/alerts")
driver.maximize_window()
wait=WebDriverWait(driver,10)

#simple alert
btn1=wait.until(EC.element_to_be_clickable((By.ID,"alertButton")))
btn1.click()
sleep(2)
alert1=wait.until(EC.alert_is_present())
alert1.accept()

#timer alert
btn2=wait.until(EC.element_to_be_clickable((By.ID,"timerAlertButton")))
sleep(5)
btn2.click()
alert2=wait.until(EC.alert_is_present())
alert2.accept()

#confirmation alert
btn3=wait.until(EC.element_to_be_clickable((By.ID,"confirmButton")))
sleep(3)
btn3.click()
alert3=wait.until(EC.alert_is_present())
alert3.accept()
result=wait.until(EC.visibility_of_element_located((By.ID,"confirmResult")))
assert "Ok" in result.text,'error'

#prompt alert
btn4=wait.until(EC.element_to_be_clickable((By.ID,"promtButton")))
btn4.click()
sleep(3)
alert5=wait.until(EC.alert_is_present())
alert5.send_keys("Heloooo")
alert5.accept()
prompt=wait.until(EC.visibility_of_element_located((By.ID,"promptResult")))
assert "Heloooo" in prompt.text,'error'
driver.quit()