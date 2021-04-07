# -*- coding:utf-8 -*-
from bases.base import Base
import pages


class SZUniversty(Base):
    def page_input_username(self, value):
        self.base_input(pages.sz_login_username, value)

    def page_input_password(self, value):
        self.base_input(pages.sz_login_password, value)

    def page_input_code(self, value):
        self.base_input(pages.sz_login_password, value)

    def page_click_submit_btn(self):
        self.base_click(pages.sz_login_submit)



