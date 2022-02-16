from selenium import webdriver

class Basepage:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get('http://www.baidu.com')

        def find_ele(self,*args):
          return self.driver.find_element(*args)






