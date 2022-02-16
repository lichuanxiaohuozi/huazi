from selenium import webdriver
import  time

from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
# 请求网址
url = "https://www.baidu.com/"
driver.get(url)
# time.sleep(3)
# driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[5]/div/div/form/span[1]/span[1]').click()
# # time.sleep(5)
# # driver.find_element_by_name('wd').click()
# time.sleep(3)
# driver.close()

# driver.find_element(By.ID,"kw").send_keys("美女")
# time.sleep(3)
# driver.close()
driver.find_element(By.ID,'kw').send_keys('刘仁娜')
driver.find_element(By.ID,'su').click()
time.sleep(5)
driver.find_element_by_xpath('/html/body/div[2]/div[4]/div[1]/div[3]/div[1]/div[2]/div/div/h3/a').click()
time.sleep(5)
handles = driver.window_handles
driver.switch_to.window(driver.window_handles[-1])
time.sleep(2)
driver.find_element_by_xpath('/html/body/div[4]/div[2]/div/dl/dd[2]/div/div[2]/a[12]').click()
time.sleep(5)

driver.switch_to.window(driver.window_handles[-1])
time.sleep(3)
driver.close()
