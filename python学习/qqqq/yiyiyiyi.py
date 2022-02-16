import HTMLTestRunnerCN
import unittest
Testcase_dir = 'C:\\Users\\EDZ\\Desktop\\python学习\\fengzhuang'
dis = unittest.defaultTestLoader.discover(Testcase_dir,'diaoyongg.py')
filename = 'C:\\Users\\EDZ\\Desktop\\python学习\\baogao\\html.HTML'
fp = open(filename,'wb')
runner = HTMLTestRunnerCN.HTMLTestRunner(stream=fp,title='测试', description="描述：")
runner.run(dis)
