
"""
封装driver
"""
from appium import webdriver


class GetDriver:
    @classmethod
    def get_driver(self):
        if self.driver is None:
            caps = {}
            # server 启动参数
            caps['platformName'] = 'Android'
            caps['platformVersion'] = '5.1'
            caps['deviceName'] = '192.168.56.101:5555'
            caps['appPackage'] = 'com.vcooline.aike'
            caps['appActivity'] = '.umanager.LoginActivity'
            # 声明driver对象
            self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', caps)
        return self.driver
    @classmethod
    def close_driver(self):
        self.driver.quit()
        self.driver=None