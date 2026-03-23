from time import sleep
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
driver=webdriver.Chrome()
driver.get("https://www.chennaisuperkings.com/")
driver.maximize_window()
actions = ActionChains(driver)
sleep(3)
img=driver.find_element(By.XPATH,"//img[@src='https://gallery.chennaisuperkings.com/PROD/GALLERY/CSKGAL_IMG2026-03-18_Image_1773839730280.png']")
actions.scroll_to_element(img).perform()
sleep(3)
for i in range(5):
    actions.send_keys(Keys.PAGE_UP).perform()
    sleep(2)