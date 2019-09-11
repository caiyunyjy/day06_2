
#定义操作类
import page
from base.bage_login import Bage


class PageLogin(Bage):
#输入用户名

    def input_username(self,username):
        self.bage_input(page.username,username)
#输入密码
    def input_password(self,password):
        self.bage_input(page.password,password)
#点击登录按钮
    def click_btn(self):
        self.bage_find(page.login_btn)
#组合方法
    def login_all(self,username,password):
        self.input_username(username)
        self.input_password(password)
        self.click_btn()