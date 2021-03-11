# -*- coding:utf-8 -*-
from tools.get_driver import GetDriver
import pages
from pages.page_pc import PagePC
from time import sleep
import allure


@allure.feature("PC官网页面流程")
class TestPC(object):
    # 创建测试PC官网页面类
    def setup_class(self):
        # 初始化driver
        self.driver = GetDriver().get_driver(pages.pc_url)
        # 获取官网页面对象
        self.pc = PagePC(self.driver)

    def teardown_class(self):
        # 退出driver
        GetDriver().quit_driver()

    @allure.story("01-悬浮框在线咨询")
    def test01_pc_consult_online(self):
        allure.dynamic.title("悬浮框在线咨询")
        sleep(0.5)
        # 点击悬浮框在线咨询
        self.pc.page_click_consult_online()
        # 断言,判断聊天框是否存在
        sleep(0.5)
        if self.pc.page_chat_box_is_exist():
            assert True
        else:
            # 不存在，截图
            self.pc.base_get_image()
            assert False

    @allure.story("02-关闭美洽弹窗")
    def test02_pc_chat_box_close(self):
        allure.dynamic.title("关闭美洽弹窗")
        # 存在，关闭聊天框
        sleep(0.5)
        try:
            # print("1-debug, 准备点击关闭美洽弹窗")
            self.pc.page_chat_box_close_btn()
            with allure.step("成功"):
                assert True
        except Exception as e:
            # 不存在，截图
            with allure.step("失败"):
                self.pc.base_get_image()
                print(e)

    @allure.story("03-悬浮框电话按钮")
    def test03_pc_tel(self):
        allure.dynamic.title("点击悬浮框电话按钮")
        # 点击悬浮框电话按钮
        self.pc.page_click_tel()
        if self.pc.page_tel_is_exist():
            # 断言, 有电话框出现
            with allure.step("成功"):
                assert True
        else:
            # 不存在，截图e
            with allure.step("失败"):
                self.pc.base_get_image()
                assert False

    @allure.story("04-悬浮框微信咨询")
    def test04_pc_wechat(self):
        allure.dynamic.title("点击悬浮框微信咨询")
        # 点击悬浮框微信咨询
        sleep(0.5)
        self.pc.page_click_wechat()
        if self.pc.page_wechat_code_is_exist():
            # 断言, 有微信二维码出现
            with allure.step("成功"):
                assert True
        else:
            with allure.step("失败"):
                # 不存在，截图e
                self.pc.base_get_image()
                assert False

    @allure.story("05-立即咨询")
    def test05_pc_consult_immediately(self):
        allure.dynamic.title("点击立即咨询")
        # 点击立即咨询
        self.pc.page_click_consult_immediately()
        try:
            # 断言,判断聊天框是否存在
            assert True == self.pc.page_chat_box_is_exist()
            # 存在，关闭聊天框
            self.pc.page_chat_box_close_btn()
        except Exception as e:
            # 不存在，截图
            self.pc.base_get_image()
            print(e)

    @allure.story("06-案例一")
    def test06_pc_demo1_detail(self):
        allure.dynamic.title("点击案例一，查看详情")
        # 点击案例一，查看详情
        self.pc.page_click_demo1_detail()
        try:
            # 断言,判断文章内容是否准确
            assert "7天，从拒赔到协议赔付27万" in self.pc.page_get_demo_detail_title()
            # 点击首页返回
            self.pc.page_click_detail_index()
        except Exception as e:
            # 不准确，截图
            self.pc.base_get_image()
            print(e)

    @allure.story("07-案例二")
    def test07_pc_demo2_detail(self):
        allure.dynamic.title("点击案例二，查看详情")
        # 点击案例二，查看详情
        self.pc.page_click_demo2_detail()
        self.pc.base_scroll(0)
        try:
            # 断言,判断文章内容是否准确
            assert "滴滴司机凌晨猝死" in self.pc.page_get_demo_detail_title()
            # 点击首页返回
            sleep(1)
            js = "window.location.href='javascript:history.go(-1)'"
            with allure.step("返回首页"):
                self.driver.execute_script(js)
        except Exception as e:
            # 不准确，截图
            self.pc.base_get_image()
            print(e)

    @allure.story("08-剩余名额")
    def test08_pc_remain_place(self):
        allure.dynamic.title("获取剩余名额内容值")
        if self.pc.page_get_remain_place():
            # 断言，获取剩余名额内容值
            with allure.step("成功"):
                assert True
        else:
            # 名额值为空，截图
            with allure.step("失败"):
                self.pc.base_get_image()
                assert False

    @allure.story("09-预约咨询")
    def test09_pc_book_consult(self, value="自动化", tel="13800000000"):
        allure.dynamic.title("预约咨询业务")
        # 预约咨询业务
        self.pc.page_book_consult(value, tel)
        sleep(0.5)
        try:
            # 断言，获取预约成功内容
            assert True == self.pc.page_get_success_content()
            # 关闭预约成功框
            self.pc.page_success_box_close()
        except Exception as e:
            # 预约失败，截图
            print("失败了")
            self.pc.base_get_image()
            print("截图成功了")
            print(e)

    @allure.story("10-返回顶部")
    def test010_pc_to_top(self):
        allure.dynamic.title("返回顶部")
        # 回到顶部
        self.pc.page_to_top()
        try:
            assert True == self.pc.page_to_top_content()
        except Exception as e:
            # 返回顶部失败，截图
            self.pc.base_get_image()
            print(e)
