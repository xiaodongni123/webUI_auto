# -*- coding:utf-8 -*-
from bases.base import Base
import pages


# 创建订单列表页面类
class PageAdminOrderList(Base):

    def page_click_order_manage(self):
        # 点击订单管理
        self.base_click(pages.order_manage)

    def page_click_order_result(self):
        # 点击理赔结果诊断
        self.base_click(pages.order_result)

    def page_input_user_nickname(self, value):
        # 清空
        self.base_find_element(pages.order_nickName).clear()
        # 输入用户昵称
        self.base_find_element(pages.order_nickName).send_keys(value)

    def page_click_search_btn(self):
        # 点击搜索
        self.base_click(pages.order_search_btn)

    def page_scroll_up(self):
        # 页面上滑
        self.base_scroll(10000)

    def page_click_view_info(self):
        # 点击查看资料
        self.base_click(pages.order_view_info)

    def page_click_reserve_explanation(self):
        # 点击预约解读
        self.base_click(pages.order_reserve_explanation)

    # 封装查看资料业务流程

    # 封装预约解读业务流程
