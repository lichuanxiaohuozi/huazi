from selenium import webdriver
#导入selenium插件
import time
#插入时间控制插件
from selenium.webdriver import ActionChains
#ActionChains是一个类（插入这个插件）
url = "https://www.baidu.com/"
#插入网址
driver = webdriver.Chrome()
#赋值driver = webdriver.Chrome
# url = "https://www.baidu.com/"
driver.get(url)
#获取方法
abc=ActionChains(driver)
# 创建动作对象
abcd = driver.find_element_by_id('lg')
time.sleep(3)
# 定位到百度的logo图片
# abc.context_click(abcd).perform()
# time.sleep(3)
abc.double_click(abcd).perform()
time.sleep(3)