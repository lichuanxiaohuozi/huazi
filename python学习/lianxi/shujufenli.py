from selenium import webdriver
import time
import xlrd

driver = webdriver.Chrome()

data = xlrd.open_workbook('C:\\Users\\EDZ\\Desktop\\python学习\\lianxi\\zzzz.xls')

table = data.sheet_by_name('Sheet1')

list = []
for i in range (0,table.nrows):
    list = table.row_values(i)
    break
print(list)
time.sleep(3)

driver.get(list[0])
time.sleep(3)

driver.find_element_by_id(list[3]).send_keys(list[4])
time.sleep(3)
driver.find_element_by_id(list[7]).click()
time.sleep(3)

for i in range (1,table.nrows):
    list = table.row_values(i)
    print(list)
    time.sleep(3)
driver.find_element_by_xpath(list[0]).click()
time.sleep(3)
driver.close()

