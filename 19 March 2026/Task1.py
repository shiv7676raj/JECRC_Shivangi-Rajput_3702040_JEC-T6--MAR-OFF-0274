from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
opts=webdriver.ChromeOptions()
opts.add_experimental_option("detach",True)
driver=webdriver.Chrome(options=opts)
driver.get("https://abc.com/")
driver.maximize_window()
obj=WebDriverWait(driver,10)
ele=obj.until(EC.presence_of_all_elements_located((By.XPATH,"//figure[@class='Image aspect-ratio--parent tile__imagecontainer']/descendant::img")))
for i in ele:
    print(i.get_attribute('src'))