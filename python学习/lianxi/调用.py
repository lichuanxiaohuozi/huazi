from fengzhuang.fengzhuang import abcd
import time
if __name__ == '__main__':
    web = abcd()
    web.open_url('https://www.baidu.com')
    ab = web.yuansu('id','kw').send_keys('麻豆')
    time.sleep(3)
    cd = web.yuansu('id','su').click()
