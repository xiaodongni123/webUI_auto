# -*- coding:utf-8 -*-
import pytest
from pages.page_admin_login import PageAdminLogin
from tools.get_driver import GetDriver
import allure
from tools.read_yaml import read_yaml
import pages


# 封装登录测试类
@allure.feature("测试登录流程")
class TestAdminLogin(object):
    def setup_class(self):
        # 获取driver
        driver = GetDriver().get_driver(pages.admin_url)
        # 初始化page中login类
        self.login = PageAdminLogin(driver)

    def teardown_class(self):
        # 退出driver
        GetDriver().quit_driver()

    @allure.story("登录")
    @pytest.mark.parametrize("title, username, password, loc, expect", read_yaml("admin_login.yaml"))
    def test01_admin_login(self, title, username, password, loc, expect):
        allure.dynamic.title(title)
        # 根据对象调用page中login业务流程方法
        self.login.page_admin_login(username, password)
        # 断言，获取登录后的文本响应
        try:
            assert "系统管理员" == self.login.base_get_text(loc)
            print("登录成功啦")
        except Exception as e:
            # 截图
            self.login.base_get_image()
            print("登录失败", e)
