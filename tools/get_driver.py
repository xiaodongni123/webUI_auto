# -*- coding:utf-8 -*-
from selenium import webdriver

# 封装获取driver类
class GetDriver(object):
    driver = None

    @classmethod
    def get_driver(cls, url):
        if cls.driver is None:
            # 如果driver不存在，将创建新的driver
            cls.driver = webdriver.Chrome()
            # 最大化浏览器
            cls.driver.maximize_window()
            # 获取url
            cls.driver.get(url)
            # 暂停3s
            # sleep(5)
        # 如果driver存在，将返回原来的driver
        return cls.driver

    @classmethod
    def quit_driver(cls):
        # 封装退出driver方法
        if cls.driver:
            # 如果driver存在，退出driver，并置空
            cls.driver.quit()
            cls.driver = None

if __name__ == '__main__':
    g = GetDriver()
    g.get_driver()
    g.quit_driver()








