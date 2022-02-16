from selenium import webdriver
import time

class abcd():
    def __init__(self):
        self.driver = webdriver.Chrome()
        time.sleep(3)

    def dwf(self, id):
        self.all = self.driver.window_handles
        self.driver.switch_to.frame(id)


    def login(self,username,pwd):
        self.driver.find_element_by_id('u').send_keys('username')
        time.sleep(3)
        self.driver.find_element_by_id('p').send_keys('pwd')
        time.sleep(3)
        self.driver.find_element_by_id('login_button')
        time.sleep(3)

        self.driver.find_element_by_id('composebtn').click()
        time.sleep(5)

    def dwf(self, id):
        self.all = self.driver.window_handles
        self.driver.switch_to.frame(id)


# if __name__ == '__main__':
#     web = abcd()
#     web.open_url('https://mail.qq.com/')
#     ab = web.yuansu('id','kw').send_keys('刘仁娜')
#     cd = web.yuansu('id','su').click()

    # def __del__(self):
    #     time.sleep(3)
    #     self.driver.close()


