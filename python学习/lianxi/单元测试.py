from selenium import webdriver
import unittest
import time

from selenium.webdriver.common.keys import Keys

class Test(unittest.TestCase):

    def setUp(self):#网址  方法
        self.driver = webdriver.Chrome()
        self.driver.get('http://www.baidu.com')

    def test1(self):
        self.driver.find_element_by_id('kw').send_keys('刘仁娜')
        time.sleep(3)
        self.driver.find_element_by_id('su').click()
        time.sleep(3)


    def test2(self):
        self.driver.find_element_by_id('kw').send_keys('李栋旭')
        time.sleep(3)
        self.driver.find_element_by_id('su').click()
        time.sleep(3)

    def tearDown(self):
        time.sleep(3)
        self.driver.quit()

# class Test2(unittest.TestCase):
#
#     def setUp(self):#网址  方法
#         self.driver = webdriver.Chrome()
#         self.driver.get('http://www.baidu.com')
#
#     def test1(self):
#         self.driver.find_element_by_id('kw').send_keys('刘')
#         time.sleep(3)
#         self.driver.find_element_by_id('su').click()
#         time.sleep(3)
#
#
#     def test2(self):
#         self.driver.find_element_by_id('kw').send_keys('李旭')
#         time.sleep(3)
#         self.driver.find_element_by_id('su').click()
#         time.sleep(3)
#
#     def tearDown(self):
#         time.sleep(3)
#         self.driver.quit()
#
#
# if __name__ == '__main__':
#     unittest.main()


