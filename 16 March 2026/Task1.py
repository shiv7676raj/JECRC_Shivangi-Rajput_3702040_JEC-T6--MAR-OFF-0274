from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

opts = webdriver.ChromeOptions()
opts.add_experimental_option('detach', True)
driver = webdriver.Chrome(options=opts)
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.maximize_window()
sleep(2)
print("Title:", driver.title)
uname = driver.find_element(By.XPATH, "//input[@name='username']")
uname.clear()
uname.send_keys("Admin")
passwd = driver.find_element(By.XPATH, "//input[@type='password']")
passwd.send_keys("admin123")
passwd.send_keys(Keys.ENTER)
sleep(2)
current_url = driver.current_url
print("Current URL:", current_url)
if "dashboard" in current_url.lower():
    print("Successful login")
driver.quit()