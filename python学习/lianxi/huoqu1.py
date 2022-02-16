# import  requests
# import  unittest
#
# class EasyBuyLogin(unittest.TestCase):
#     def test01(self):
#         url = 'http://localhost:8080/EasyBuy/Login'
#
#         data = 'loginame=admin&password=123456&action=login'
#
#
#
#
#         response = requests.request('POST',url,params=data)
#         print(response.text)
#
#         result = response.json()['status']
#         print(result)
#
#         self.assertEqual(1,result)
#         self.assertIn('登陆成功',response.text)
#         self.assertTrue('操作成功'in response.text)
#
#
#         if __name__ == '__main__':
#             unittest.main





import requests
import unittest
import json
from lianxi import HTMLTestRunnerCN



class interfacetest01(unittest.TestCase):
    #实时天气查询接口
    def test01(self):
        url = 'https://tianqiapi.com/api'
        data = 'version=v6&appid=73691227&appsecret=123456'
        response = requests.request('GET',url,params=data)
        print(response.json())

#文件路径
Testcase_dir = 'C:\\Users\\EDZ\\Desktop\\python学习\\lianxi'
#覆盖该文件路径下的文件
dis = unittest.defaultTestLoader.discover(Testcase_dir,'huoqu1.py')
filename = 'C:\\Users\\EDZ\\Desktop\\python学习\\lianxi\\huoqu1.html'
fp = open(filename, 'wb')
runner = HTMLTestRunnerCN.HTMLTestRunner(
stream=fp,
title='接口测试报告',
description='用例执行情况：')
#runner.run(testunit)
runner.run(dis)
fp.close()
