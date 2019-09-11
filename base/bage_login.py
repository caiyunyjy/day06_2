#导包

#定义类
from appium import webdriver
from selenium.webdriver.support.wait import WebDriverWait


class Bage:
    def __init__(self,driver):
        self.driver = driver #为什么必须以参数的形式传入driver

#定义查找方法
    def bage_find(self,loc,timeout=30,poll=0.5):
        return (WebDriverWait(self.driver,timeout=timeout,poll_frequency=poll).
                until(lambda x:x.find_element(*loc)))
#定义input 方法
    def bage_input(self,loc,word):
        el =self.bage_find(loc)
        el.clear()
        el.send_keys(word)
#定义点击方法
    def bage_click(self,loc):
        self.bage_find(loc).click()

