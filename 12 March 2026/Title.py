from selenium import webdriver
opts=webdriver.ChromeOptions()
opts.add_experimental_option('detach', True)
driver=webdriver.Chrome(options=opts)
driver.get('https://www.amazon.com')
driver.maximize_window()
print(f'Current uRL: {driver.current_url}')
print(f'Title: {driver.title}')
print(f'Browser name:{driver.name}')