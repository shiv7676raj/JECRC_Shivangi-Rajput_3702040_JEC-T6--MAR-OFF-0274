from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
opts = webdriver.ChromeOptions()
opts.add_experimental_option('detach', True)
driver = webdriver.Chrome(options=opts)
driver.get("https://demoqa.com/radio-button")
driver.maximize_window()
sleep(2)
print("Title:",driver.title)
btn=driver.find_element(By.XPATH,"//input[@id='yesRadio']")
btn.click()
sleep(2)
result = driver.find_element(By.CLASS_NAME,"text-success")
print("Result:",result.text)
print("CLass:",btn.get_attribute("class"))
print("ID:",btn.get_attribute("id"))
print("Current URL:",driver.current_url)
driver.quit()