from fengzhuang import webdriver
import unittest
import time

class login(unittest.TestCase):
     '''qq邮箱'''
     def setUp(self):
         self.driver = webdriver.Chrome()
         self.driver.get('https://mail.qq.com/')
         time.sleep(3)
     def test1(self):
         self.driver.switch_to.frame('login_frame')
         time.sleep(3)
         self.driver.find_element_by_xpath('//*[@id="switcher_plogin"]').click()
         time.sleep(3)
         self.driver.find_element_by_id('u').send_keys('2592754217')
         time.sleep(3)
         self.driver.find_element_by_id('p').send_keys('ysj12345')
         time.sleep(3)
         self.driver.find_element_by_id('login_button').click()
         time.sleep(10)
         self.driver.find_element_by_id('composebtn').click()
         time.sleep(10)


     def tearDown(self):
         self.driver.close()
         time.sleep(3)
if __name__ == '__main__':
    unittest.main()




