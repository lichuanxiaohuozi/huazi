from selenium import webdriver
import time

class yi:
    def __init__(self):
        self.driver = webdriver.Chrome()
        time.sleep(3)
    def kj(self,id):#定位框架
        self.kj = self.driver.switch_to.frame(id)
    def bq(self,XPth):#定位biaoqian
        self.aa = self.driver.window_handles
        self.xbq = self.driver.switch_to_window(self.aa[-1])

    # def ss(self, ssk, zhi):
    #     return self.driver.find_element(ssk, zhi)
    def login(self,username,pwd):
        self.driver.find_element_by_id('u').send_keys('username')
        time.sleep(3)
        self.driver.find_element_by_id('p').send_keys('pwd')
        time.sleep(3)
        self.driver.find_element_by_id('login_button').click()

