import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
folder=os.path.join(os.getcwd(), 'Screenshots')
os.makedirs(folder, exist_ok=True)
driver = webdriver.Chrome()
driver.get("https://in.pinterest.com/")
driver.maximize_window()
actions = ActionChains(driver)
sleep(3)
driver.save_screenshot(f'{folder}/full_page.png')
sleep(3)
ele=driver.find_element(By.XPATH,"(//div[@class='ADXRXN AsRsEE'])[3]/descendant::img")
#Another XPATH we can give---//img[contains(@alt,'Photo of a woman')]
actions.scroll_to_element(ele).perform()
sleep(2)
ele.screenshot(f'{folder}/ele_shot.png')
sleep(3)