# -*- coding:utf-8 -*-
from time import sleep
from bases.base import Base
import pages
import allure


# 创建PC官网页面类
class PagePC(Base):
    @allure.step("点击右边的在线咨询")
    def page_click_consult_online(self):
        # 点击右边的在线咨询
        self.base_find_element(pages.pc_consult_online, timeout=3).click()

    @allure.step("判断聊天对话框是否存在")
    def page_chat_box_is_exist(self):
        # 切换iframe
        self.base_switch_frame(pages.pc_chat_box_frame_id)
        # 聊天对话框是否存在
        return self.base_element_is_exist(pages.pc_chat_box_close_btn)

    @allure.step("关闭美洽聊天对话框")
    def page_chat_box_close_btn(self):
        # 对美洽聊天对话框点击关闭
        self.base_find_element(pages.pc_chat_box_close_btn).click()
        # 返回主目录
        self.base_frame_switch_to_default()

    @allure.step("点击电话按钮")
    def page_click_tel(self):
        # 点击电话按钮
        self.base_find_element(pages.pc_consult_on_tel).click()

    @allure.step("判断是否出现电话")
    def page_tel_is_exist(self):
        sleep(0.5)
        # 出现电话
        return self.base_element_is_exist(pages.pc_tel_box)

    @allure.step("点击微信咨询")
    def page_click_wechat(self):
        sleep(0.5)
        # 点击微信咨询
        self.base_find_element(pages.pc_wechat_consult).click()

    @allure.step("判断是否出现微信二维码")
    def page_wechat_code_is_exist(self):
        sleep(0.5)
        # 出现微信二维码
        return self.base_element_is_exist(pages.pc_wechat__box)

    @allure.step("点击立即咨询")
    def page_click_consult_immediately(self):
        # 页面下滑
        self.base_scroll(968)
        sleep(0.5)
        # 点击立即咨询
        self.base_find_element(pages.pc_consult_immediately, timeout=3).click()

    @allure.step("点击案例一查看详情")
    def page_click_demo1_detail(self):
        # 页面下滑
        self.base_scroll(2518)
        sleep(0.5)
        # 点击案例一，查看详情
        self.base_find_element(pages.pc_demo1_view_detail, timeout=3).click()

    @allure.step("获取案例详情页标题内容")
    def page_get_demo_detail_title(self):
        # 获取案例详情页标题内容
        return self.base_get_text(pages.pc_demo_detail_title_text)

    @allure.step("点击案例详情页返回")
    def page_click_detail_index(self):
        sleep(0.1)
        # 点击首页返回
        self.base_find_element(pages.pc_demo_detail_back_btn).click()

    @allure.step("点击案例二查看详情")
    def page_click_demo2_detail(self):
        sleep(0.5)
        # 页面下滑
        self.base_scroll(2518)
        sleep(0.5)
        # 点击案例二，查看详情
        self.base_find_element(pages.pc_demo2_view_detail, timeout=3).click()

    @allure.step("获取剩余名额内容值")
    def page_get_remain_place(self):
        sleep(0.5)
        # 页面下滑
        self.base_scroll(200)
        # 获取剩余名额内容值
        return self.base_element_is_exist(pages.pc_remain_place)

    """预约咨询内容"""
    def page_choose_problem_type(self):
        # 选择问题类型
        self.base_find_element(pages.pc_choose_problem_type).click()
        self.base_find_element(pages.pc_problem_type_refuse).click()

    def page_input_username(self, value):
        # 清空
        self.base_find_element(pages.pc_username).clear()
        # 输入用户名
        self.base_find_element(pages.pc_username).send_keys(value)

    def page_input_tel_num(self, tel):
        # 清空
        self.base_find_element(pages.pc_tel_num).clear()
        # 输入电话号码
        self.base_find_element(pages.pc_tel_num).send_keys(tel)

    def page_click_submit_btn(self):
        # 点击马上预约
        self.base_find_element(pages.pc_submit_btn).click()

    def page_get_success_content(self):
        # 获取成功预约内容
        return self.base_element_is_exist(pages.pc_success_content)

    def page_success_box_close(self):
        # 关闭预约成功框
        self.base_find_element(pages.pc_success_btn_close).click()

    @allure.step("返回顶部")
    def page_to_top(self):
        # 返回顶部
        self.base_find_element(pages.pc_to_top).click()

    @allure.step("返回顶部成功")
    def page_to_top_content(self):
        # 返回顶部成功内容
        return self.base_element_is_exist(pages.pc_to_top_content)

    # 预约咨询业务代码合并
    @allure.step("预约咨询业务")
    def page_book_consult(self, value, tel):
        with allure.step("选择问题类型"):
            self.page_choose_problem_type()
        with allure.step("输入用户名"):
            self.page_input_username(value)
        with allure.step("输入联系电话"):
            self.page_input_tel_num(tel)
        with allure.step("点击立即预约"):
            self.page_click_submit_btn()



