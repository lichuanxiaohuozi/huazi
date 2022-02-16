import unittest

from aaaa import webdriver
import time


class login(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        time.sleep(3)
        self.driver.get('http://www.baidu.com')
        time.sleep(3)
    def test01(self):
        self.driver.find_element_by_id('kw').send_keys('QQ邮箱')
        time.sleep(3)
        self.driver.find_element_by_id('su').click()
        time.sleep(3)
        self.driver.find_element_by_xpath('//*[@id="1"]/h3/a[1]').click()
        time.sleep(10)
        self.driver.switch_to_window(self.aa[-1])
        self.driver.switch_to.frame('login_frame')
        time.sleep(5)
        self.driver.find_element_by_id('kw').send_keys('2592754217')
        time.sleep(3)
        self.driver.find_element_by_id('su').send_keys('ysj12345')
        time.sleep(3)
        self.driver.find_element_by_id('login_button').click()
        time.sleep(3)





        # self.handles = self.driver.window_handles
        # self.driver.switch_to.window(self.handles[-1])
        # self.driver.find_element_by_xpath('//*[@id="1"]/h3/a[1]').click()


