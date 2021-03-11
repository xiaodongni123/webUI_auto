# -*- coding:utf-8 -*-
from selenium.webdriver.common.by import By

"""以下是后台管理系统的元素"""
admin_url = "https://admin.haohuipei.com/"

# 登录页元素
login_username = By.CSS_SELECTOR, "#userName"  # 用户名
login_password = By.CSS_SELECTOR, "#password"  # 密码
login_submit_btn = By.CSS_SELECTOR, ".ant-btn"  # 登录按钮

# 订单列表页元素
order_manage = By.XPATH, "//div[@class='ant-menu-submenu-title']//span[text()='订单管理']"  # 订单管理
order_result = By.XPATH, "//a/span[text()='理赔结果诊断']"  # 理赔结果诊断
order_nickName = By.CSS_SELECTOR, "#nickName"  # 用户昵称
order_search_btn = By.CSS_SELECTOR, ".Search"  # 搜索按钮
order_view_info = By.XPATH, "//span[text()='查看资料']"  # 查看资料
order_reserve_explanation = By.XPATH, "//span[text()='预约解读']"  # 预约解读


"""以下是官网和投放页的元素"""
# PC官网
pc_url = "https://www.haohuipei.com/"
pc_consult_online = By.XPATH, "//span[text()='在线咨询']"  # 在线咨询
pc_chat_box_frame_id = "chat" # 美洽咨询框frame
pc_chat_box_close_btn = By.XPATH, "//i[@class='iconfont__IconFont-sc-1aa14be-0 erPEYs icondropdown close']"  # 美洽咨询框关闭按钮
pc_consult_on_tel = By.XPATH, "//span[text()='电话咨询']"  # 电话咨询
pc_tel_box = By.CSS_SELECTOR, ".RightMenu_p1__1x6CJ"  # 电话咨询弹出框
pc_wechat_consult = By.XPATH, "//span[text()='微信咨询']"  # 微信咨询
pc_wechat__box = By.CSS_SELECTOR, ".RightMenu_qrcodeHover__3xXdS"  # 微信咨询二维码框
pc_consult_immediately = By.CSS_SELECTOR, ".home_hotline__jKjwX"  # 立即咨询
pc_demo1_view_detail = By.XPATH, "//div[contains(text(), '7天')]/../div[6]/span/a"  # 案例1查看详情
pc_demo2_view_detail = By.XPATH, "//div[contains(text(), '滴滴')]/../div[6]/span/a"  # 案例2查看详情
pc_demo_detail_title_text = By.XPATH, "//h2"  # 案例详情页内标题
pc_demo_detail_back_btn = By.CSS_SELECTOR, ".case_Back__3KApR"  # 案例详情页内返回按钮
pc_remain_place = By.XPATH, "//div[@class='Appointment_appointmentContent__12WwR']/div/div/div[2]/h3"  # 剩余名额
pc_choose_problem_type = By.CSS_SELECTOR, "#rc_select_0"  # 选择问题类型
pc_problem_type_refuse = By.CSS_SELECTOR, "[title='被拒赔']"  # 被拒赔
pc_username = By.CSS_SELECTOR, "#basic_userName"  # 用户名
pc_tel_num = By.CSS_SELECTOR, "#basic_cellphone"  # 电话号码
pc_submit_btn = By.CSS_SELECTOR, "[type='submit']"  # 马上预约
pc_success_content = By.CSS_SELECTOR, ".Submit_successIcon__2YxUN"  # 预约成功图片
pc_success_btn_close = By.CSS_SELECTOR, ".Submit_closeBtn__jXJ9M"  # 关闭预约成功框
pc_to_top = By.CSS_SELECTOR, ".RightMenu_arrow__2NMd8"  # 回到顶部
pc_to_top_content = By.CSS_SELECTOR, "[alt='好慧赔']"  # 回到顶部后获取顶部logo







