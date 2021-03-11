# -*- coding:utf-8 -*-
from bases.base import Base
import pages
from time import sleep
import allure


# 封装后台管理系统登录页面类,继承Base
class PageAdminLogin(Base):
    def page_input_username(self, username):
        # 输入用户名
        self.base_input(pages.login_username, username)

    def page_input_password(self, password):
        # 输入密码
        self.base_input(pages.login_password, password)

    def page_click_login_btn(self):
        # 点击登录按钮
        self.base_click(pages.login_submit_btn)

    def page_admin_login(self, username, password):
        # 封装业务流程，供脚本层调用
        sleep(5)
        with allure.step("输入用户名"):
            self.page_input_username(username)
        with allure.step("输入密码"):
            self.page_input_password(password)
        with allure.step("点击登录按钮"):
            self.page_click_login_btn()
