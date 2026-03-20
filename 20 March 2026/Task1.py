from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

opt= webdriver.ChromeOptions()
opt.add_experimental_option("detach", True)
driver=webdriver.Chrome(options=opt)
driver.get(r'C:\Users\HP\PycharmProjects\PythonProject\playlist.html')
driver.maximize_window()
songs_list=driver.find_element(By.ID,'songs')
select=Select(songs_list)
opt=select.options
for i in opt:
    text=i.text
    if 'Girl' in text or 'Love' in text:
        print(text)
        select.select_by_visible_text(text)
driver.find_element(By.XPATH,'//button[text()="Add to Playlist"]').click()
sleep(3)
driver.quit()