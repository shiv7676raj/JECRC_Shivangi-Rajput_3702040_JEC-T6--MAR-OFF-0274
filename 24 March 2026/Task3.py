from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver=webdriver.Chrome()
driver.get("https://demoqa.com/browser-windows")
driver.maximize_window()
wait=WebDriverWait(driver,10)
parent_window=driver.current_window_handle

#new tab
tab_btn=wait.until(EC.element_to_be_clickable((By.ID,"tabButton")))
tab_btn.click()
wait.until(EC.number_of_windows_to_be(2))
all_windows=driver.window_handles
for i in all_windows:
    if i!=parent_window:
        driver.switch_to.window(i)
        break

text1=wait.until(EC.visibility_of_element_located((By.ID,"sampleHeading")))
assert "This is a sample page" in text1.text
driver.close()
driver.switch_to.window(parent_window)

#new window
win_btn=wait.until(EC.element_to_be_clickable((By.ID,"windowButton")))
win_btn.click()
wait.until(EC.number_of_windows_to_be(2))
all_windows=driver.window_handles
for i in all_windows:
    if i!=parent_window:
        driver.switch_to.window(i)
        break

text2=wait.until(EC.visibility_of_element_located((By.ID,"sampleHeading")))
assert "This is a sample page" in text2.text
driver.close()
driver.switch_to.window(parent_window)

#new window msg
# msg_btn=wait.until(EC.element_to_be_clickable((By.ID,"messageWindowButton")))
# msg_btn.click()
# wait.until(EC.number_of_windows_to_be(2))
# all_windows=driver.window_handles
# for i in all_windows:
#     if i!=parent_window:
#         driver.switch_to.window(i)
#         break
#
# msg = wait.until(EC.visibility_of_element_located((By.TAG_NAME,"body")))
# assert "Knowledge increases by sharing but not by saving" in msg
# driver.close()
# driver.switch_to.window(parent_window)
driver.quit()