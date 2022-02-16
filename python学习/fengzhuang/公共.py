# from selenium import webdriver
# import time
#
# class Gonggong:
#     def __init__(self):
#         self.driver = webdriver.Chrome()
#
#     def delay(self):
#         self.driver.implicitly_wait(5)
#
#     def url(self,url):
#         self.driver.get(url)
#     def yuansu(self,yuansu,value):
#
#         return self.driver.find_element(yuansu,value)
#     def __del__(self):
#         time .sleep(3)
#         self.driver.close()





from selenium import webdriver
import unittest
import time

from selenium.webdriver.common.keys import Keys

class Test(unittest.TestCase):

    def setUp(self):#网址  方法
        self.driver = webdriver.Chrome()
        self.driver.get('http://www.baidu.com')

    def test1mokuai(self):
        mokuai = self.driver.switch_to.frame(self.driver.find_element_by_xpath('//*[@id="login_frame"]'))
        return mokuai
        time.sleep(3)

    def test2denglu(self):
        denglu = self

