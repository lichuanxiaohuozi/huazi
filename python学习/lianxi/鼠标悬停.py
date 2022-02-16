from selenium import webdriver
import time
from selenium.webdriver import ActionChains
url = 'https://www.jd.com/'
driver = webdriver.Chrome()
driver.get(url)

# mylist = driver.find_element_by_xpath('//*[@id="J_cate"]/ul/li[2]')
# mylist = driver.find_elements_by_css_selector('li.cate_menu_item')
mylist = driver.find_elements_by_class_name('cate_menu_item')
time.sleep(3)
abc = ActionChains(driver)
##J_cate > ul > li:nth-child(1)#J_cate > ul#J_cate#J_cate > ul > li:nth-child(2)
#

for abcd in mylist :
    abc.move_to_element(abcd).perform()
    time.sleep(3)
