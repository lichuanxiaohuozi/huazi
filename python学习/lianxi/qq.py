from selenium import webdriver

import  time

from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

url = "https://www.baidu.com/"
driver.get(url)
driver.find_element(By.ID,'kw').send_keys('QQ邮箱')
driver.find_element(By.ID,'su').click()
time.sleep(3)
driver.find_element_by_xpath('/html/body/div[2]/div[4]/div[1]/div[3]/div[1]/h3/a[1]').click()
handles = driver.window_handles
driver.switch_to.window(driver.window_handles[-1])
time.sleep(3)
# driver.find_element_by_xpath('//*[@id="login"]')

driver.switch_to.frame(driver.find_element_by_xpath('//*[@id="login_frame"]'))#第一框架
time.sleep(3)
driver.find_element_by_xpath('//*[@id="switcher_plogin"]').click()#点击输入账号

driver.find_element_by_xpath('//*[@id="u"]').send_keys('2592754217')#输入账号

driver.find_element_by_xpath('//*[@id="p"]').send_keys('ysj12345')#输入密码

driver.find_element_by_xpath('//*[@id="login_button"]').click()#点击登入
time.sleep(3)

driver.find_element_by_xpath('//*[@id="composebtn"]').click()#点击写信
time.sleep(3)


driver.switch_to.frame(driver.find_element_by_xpath('//*[@id="mainFrame"]'))# #第二框架

time.sleep(3)

driver.find_element_by_xpath('//*[@id="toAreaCtrl"]/div[2]/input').send_keys('1027579996@qq.com')#输入收件人
time.sleep(3)

driver.find_element_by_name('UploadFile').send_keys('c:\eula.1028.txt')#添加附件
time.sleep(3)

driver.switch_to.frame(driver.find_element_by_class_name('qmEditorIfrmEditArea'))#正文框架
time.sleep(3)
driver.find_element_by_xpath('/html/body').send_keys('ainiaini')#输入正文
time.sleep(3)
driver.switch_to.parent_frame()#返回上一层框架
time.sleep(3)
driver.find_element_by_xpath('//*[@id="toolbar"]/div/a[1]').click()#点击发送
time.sleep(3)

