#To Open Chrome browser
from selenium import webdriver
from selenium.webdriver.support.expected_conditions import title_is

#from time import sleep
opts=webdriver.ChromeOptions()
opts.add_experimental_option('detach', True)
driver=webdriver.Chrome(options=opts)
#sleep(5)
# driver=webdriver.Edge()
# sleep(5)
# driver=webdriver.Firefox()
# sleep(5)
driver.get('https://www.amazon.com')
driver.maximize_window()
# sleep(2)
# driver.minimize_window()
# sleep(2)
# driver.back()
# sleep(2)
# driver.forward()
# sleep(2)
# driver.refresh()
# sleep(2)
#driver.close()
driver.quit()
