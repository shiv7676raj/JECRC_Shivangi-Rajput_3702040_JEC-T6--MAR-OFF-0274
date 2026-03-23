from time import sleep
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
#Drag and drop
# driver=webdriver.Chrome()
# driver.get("https://the-internet.herokuapp.com/drag_and_drop")
# driver.maximize_window()
# sleep(2)
# action=ActionChains(driver)
# origin=driver.find_element(By.ID,'column-a')
# target=driver.find_element(By.ID,'column-b')
# action.drag_and_drop(origin,target).perform()
# sleep(3)

#mouse hover
# driver=webdriver.Chrome()
# driver.get("https://supertails.com/")
# driver.maximize_window()
# actions = ActionChains(driver)
# dog=driver.find_element(By.XPATH,"(//span[contains(text(),'Dogs')])[1]")
# sleep(2)
# actions.move_to_element(dog).perform()
# sleep(3)

# driver=webdriver.Chrome()
# driver.get("https://supertails.com/")
# driver.maximize_window()
# actions = ActionChains(driver)
# sleep(3)
# cat=driver.find_element(By.XPATH,"//div[@data-ganame='Breed 5']")
# actions.scroll_to_element(cat).perform()
# sleep(3)
# # click-left click of mouse
# # context click-right click of mouse
# # scroll to(goes to a particular pixel value from the pixel u wrote the code)
# # scroll by(goes to points given for x and y axis )
# # scroll up-negative
# # scroll down-positive
# actions.scroll_by_amount(0,-1500).perform()
# sleep(3)

# driver=webdriver.Chrome()
# driver.get("https://demoqa.com/droppable")
# driver.maximize_window()
# sleep(2)
# action=ActionChains(driver)
# o=driver.find_element(By.ID,'draggable')
# t=driver.find_element(By.ID,'droppable')
# action.drag_and_drop(o,t).perform()
# sleep(3)
# assert 'Dropped!'==t.text,'Didnt drop'
# print('Success!')


# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# opts=webdriver.ChromeOptions()
# opts.add_experimental_option("detach",True)
# driver=webdriver.Chrome(options=opts)
# driver.get("https://demoqa.com/droppable")
# driver.maximize_window()
# obj=WebDriverWait(driver,10)
# btn=obj.until(EC.element_to_be_clickable((By.ID,'droppableExample-tab-preventPropogation')))
# btn.click()
# action=ActionChains(driver)
# o=obj.until(EC.presence_of_element_located((By.ID,'dragBox')))
# outer=obj.until(EC.presence_of_element_located((By.ID,'notGreedyDropBox')))
# inner=obj.until(EC.presence_of_element_located((By.ID,'notGreedyInnerDropBox')))
# action.drag_and_drop(o,outer).perform()
# action.drag_and_drop(o,inner).perform()
# # assert 'Dropped!'==t.text,'Didnt drop'
# # print('Success!')
# driver.quit()

#keyboard actions
# driver=webdriver.Chrome()
# driver.get("https://supertails.com/")
# driver.maximize_window()
# actions = ActionChains(driver)
# # actions.send_keys(Keys.PAGE_DOWN).perform()
# # sleep(2)
# # actions.send_keys(Keys.PAGE_UP).perform()
# # sleep(2)
# actions.key_down(Keys.CONTROL).send_keys('a').perform()
# sleep(2)
# actions.key_up(Keys.CONTROL).perform()
# sleep(2)

# driver=webdriver.Chrome()
# driver.get(r"C:\Users\HP\PycharmProjects\PythonProject\address.html")
# driver.maximize_window()
# actions = ActionChains(driver)
# present=driver.find_element(By.ID,'presentAddress')
# permanent=driver.find_element(By.ID,'permanentAddress')
# present.send_keys('JECRC, Jaipur, RJ')
# sleep(2)
# present.click()
# actions.key_down(Keys.CONTROL).send_keys('a').key_up(Keys.CONTROL).perform()
# sleep(2)
# actions.key_down(Keys.CONTROL).send_keys('c').key_up(Keys.CONTROL).perform()
# permanent.click()
# sleep(2)
# actions.key_down(Keys.CONTROL).send_keys('v').key_up(Keys.CONTROL).perform()
# sleep(3)

driver=webdriver.Chrome()
driver.get(r"C:\Users\HP\PycharmProjects\PythonProject\index1.html")
driver.maximize_window()
actions = ActionChains(driver)
driver.find_element(By.ID,'password').send_keys("nik")
sleep(2)
show_pwd=driver.find_element(By.ID,'eyeBtn')
actions.click_and_hold(show_pwd).perform()
sleep(2)
actions.release().perform()
sleep(2)