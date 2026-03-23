from time import sleep
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
opts=webdriver.ChromeOptions()
opts.add_experimental_option("detach",True)
driver=webdriver.Chrome(options=opts)
driver.get("https://www.myntra.com/")
driver.maximize_window()
obj=WebDriverWait(driver,10)
actions = ActionChains(driver)
women=obj.until(EC.presence_of_element_located((By.XPATH,"(//a[text()='Women'])[1]")))

actions.move_to_element(women).perform()

btn=obj.until(EC.element_to_be_clickable((By.XPATH,"//div[@data-group='women']//ul//li[4]")))
btn.click()
product=obj.until(EC.presence_of_element_located((By.XPATH,"//ul[@class='results-base']//li[5]")))

actions.scroll_to_element(product).perform()
driver.quit()