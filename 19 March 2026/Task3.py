from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

opt=webdriver.ChromeOptions()
opt.add_experimental_option("detach", True)
driver=webdriver.Chrome(options=opt)
driver.get("https://www.amazon.in/")
driver.maximize_window()
wait=WebDriverWait(driver, 10)
search=wait.until(EC.visibility_of_element_located((By.ID,"twotabsearchtextbox")))
search.send_keys("laptops")
suggestions=wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR,"div.s-suggestion")))
suggestions[3].click()
sort=wait.until(EC.visibility_of_element_located((By.XPATH,"//select[@id='s-result-sort-select']/descendant::option[5]")))
sort.click()
free=wait.until(EC.visibility_of_element_located((By.XPATH,"//li[@id='p_n_free_shipping_eligible/205563695031']/descendant::div/descendant::i")))
free.click()
title=wait.until(EC.visibility_of_element_located((By.XPATH,"//div[@class='puisg-row']/descendant::h2")))
print(title.text)
price=wait.until(EC.visibility_of_element_located((By.XPATH,"//span[@class='a-price-whole']")))
print(price.text)
driver.quit()