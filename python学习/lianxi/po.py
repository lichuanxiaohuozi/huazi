from selenium.webdriver.common.by import By
from lianxi.basepage import Basepage

class Baidupage(Basepage):

    baidushurukuang= (By.ID,"kw")
    baiduyixiadianji = (By.ID,"su")

    def get_text_obj(self):
        ele = self.find_ele(*Baidupage.baidushurukuang)
        return abcd
    def get_submit_obj(self):
        ele = self.find_ele(*Baidupage.baiduyixiadianji)
        return  abcd
    def search(self,searsh_string):
        self.get_text_obj().send_keys(searsh_string)
        self.get_submit_obj().click()
