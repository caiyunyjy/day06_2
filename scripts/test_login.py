
#定义测试类


import pytest

from page.page_in import PageIn

from tools.get_driver import GetDriver
from tools.read_yaml import read_yaml


def get_data():
    arrs = []
    for data in read_yaml("data.yaml").values():
        arrs.append((data.get("username"), data.get("password")))
    return arrs

class TestLogin:
#开始方法
    def setup_class(self):
        #做到实例化page对象或就初始化driver对象，所以page里要有init方法,或者bage类里有也行继承过来
        #实例化page对象
        self.login =PageIn().get_page_login()
#关闭方法
    def teardown_class(self):
        #常见的坑  一定要用封装的关闭方法关闭，因为只有封装的方法才有手动置空driver
        GetDriver.close_driver()
#登录测试方法
    @pytest.mark.parametrize("username,password",get_data())
    def test_login(self,username,password):
        self.login.login_all(username,password)

# pytest.main("-s test_login.py")