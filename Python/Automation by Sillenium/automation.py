from selenium import webdriver

chrome_driver = webdriver.Chrome('chromedriver')
print(chrome_driver)

chrome_driver.maximize_window()
chrome_driver.get('https://www.seleniumeasy.com/test/basic-first-form-demo.html')


assert 'Show Message' in chrome_driver.page_source

user_message = chrome_driver.find_element_by_id('user-message')
user_message.clear()
user_message.send_keys('Automated Text Sending')

