import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# drive
driver = webdriver.Firefox()
driver.get('http://www.baidu.com/')
assert "百度" in driver.title
print(driver.title)

# search&input
elem = driver.find_element_by_name("wd")
elem.send_keys("数据分析")
elem.send_keys(Keys.RETURN)

l1 = driver.find_element_by_tag_name('link')
print(l1.get_attribute('src'))

# shot&loadout
'''driver.save_screenshot('baidu.png')
driver.close()
driver.quit()'''
