from selenium import webdriver
for i in range(3):
    if i==0:
        driver=webdriver.Chrome()
        driver.get('https://www.geeksforgeeks.org/')
        driver.maximize_window()
        driver.close()
    elif i==1:
        driver=webdriver.Edge()
        driver.get('https://www.amazon.com')
        driver.maximize_window()
        driver.close()
    else:
        driver=webdriver.Firefox()
        driver.get('https://www.google.com')
        driver.maximize_window()
        driver.close()
