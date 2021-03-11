# -*- coding:utf-8 -*-
from time import strftime
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
import time
import allure

# 创建Base基类
class Base(object):
    def __init__(self, driver):
        # 初始化driver
        self.driver = driver

    # 封装查找元素方法
    def base_find_element(self, loc, timeout=30, poll=0.5):
        """
        :param loc: 查找元素的位置
        :param timeout: 查找元素超时时间
        :param poll: 查找元素的频率
        :return: 返回查找元素对象
        """
        # 显示等待
        return (WebDriverWait(self.driver,
                              timeout=timeout,
                              poll_frequency=poll).until(lambda x: x.find_element(*loc)))

    # 封装输入元素方法，首先清空元素，其次输入
    def base_input(self, loc, value):
        # 清空
        self.base_find_element(loc).clear()
        # 输入
        self.base_find_element(loc).send_keys(value)

    # 封装点击元素方法
    def base_click(self, loc):
        self.base_find_element(loc).click()

    # 封装获取页面文本方法
    def base_get_text(self, loc):
        return self.base_find_element(loc).text

    # 封装截图方法
    def base_get_image(self):
        self.driver.get_screenshot_as_file("./image/{}.png".format(time.strftime("%Y_%m_%d %H_%M_%S")))

    # 封装元素是否存在
    def base_element_is_exist(self, loc):
        try:
            self.base_find_element(loc, timeout=2)
            return True  # 表示元素存在
        except:
            return False  # 表示元素不存在

    # 封装页面直接下滑距离，有惯性
    def base_scroll(self, height):
        # 0:左边距，水平滚动条
        # height：上边距，垂直滚动条
        js = "window.scrollTo(0, {})".format(height)
        self.driver.execute_script(js)

    # 封装页面定点距离上下滑动
    def base_actions_drag_and_drop(self, loc1, loc2):
        # 确定拖拽目标的起点
        source = self.base_find_element(loc1)
        # 确定拖拽目标的终点
        target = self.base_find_element(loc2)
        # 实例ActionChains对象,形成动作链接并执行
        ActionChains(self.driver).drag_and_drop(source, target).perform()

    # 封装切换frame
    def base_switch_frame(self, loc):
        self.driver.switch_to.frame(loc)

    # 返回主目录
    def base_frame_switch_to_default(self):
        self.driver.switch_to.default_content()




