from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
opts=webdriver.ChromeOptions()
opts.add_experimental_option("detach",True)
driver=webdriver.Chrome(options=opts)
driver.get("https://abc.com/")
driver.maximize_window()
#implicitly_wait->global variable and gives time in seconds to find an
# element in the dom structure and if the element is not found in that
# given time it will throw an exception(NoSuchElementFound)
# driver.implicitly_wait(20)
# ele=driver.find_element(By.XPATH,"(//a[@class='AnchorLink']/parent::li/descendant::img)[1]")
# print(ele.get_attribute('src'))

#Explicitly_wait->wait for the element until a condition is satisfied and it gets confined
# to that element as it wait for the condition to be satisfied
#Need to import two things for it->webdriver_wait and expected_conditions
#always throw TimeOutError exception
#fluent wait part of this
obj=WebDriverWait(driver,10,poll_frequency=200)
submit=obj.until(EC.element_to_be_clickable((By.ID,'button')))
submit.click()
driver.quit()