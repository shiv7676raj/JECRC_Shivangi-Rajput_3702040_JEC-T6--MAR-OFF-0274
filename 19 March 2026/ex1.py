from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from selenium.webdriver.support.select import Select
opts=webdriver.ChromeOptions()
opts.add_experimental_option("detach",True)
driver=webdriver.Chrome(options=opts)
# driver.get("https://abc.com/")
# driver.maximize_window()
# obj=WebDriverWait(driver,10)
# loading=obj.until(EC.invisibility_of_element_located((By.ID,'preloader-animated_svg__svg3')))
# title_abc=driver.find_element_by_id(By.XPATH,'//span[text()="ABC SHOWS, SPECIALS & MORE"]')
# assert 'SPECIALS' in title_abc.text,'the text not present'
# driver.get('https://demoqa.com/dynamic-properties')
# driver.maximize_window()
# wait=WebDriverWait(driver,6)
# en_before=driver.find_element(By.ID,'enableAfter')
# print(en_before.is_enabled())
# btn=wait.until(EC.element_to_be_clickable((By.ID,'enableAfter')))
# if btn.is_enabled():
#     btn.click()
#     print(btn.text)
# vis=wait.until(EC.visibility_of_element_located((By.ID,'visibleAfter')))
# vis.click()
driver.get("https://demo.mobiscroll.com/select/multiple-select")
driver.maximize_window()
multi_drop=driver.find_element(By.XPATH,'//select[@id="multiple-select-context"]')
select=Select(multi_drop)
if select.is_multiple:
    select.select_by_value("1")
    select.select_by_index(3)
    select.select_by_visible_text("Movies, Music & Games")
sleep(4)
select.deselect_by_index(3)
select.deselect_all()
print(select.first_selected_option)
print(select.all_selected_options)

driver.quit()