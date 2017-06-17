#coding=utf-8
from Util.ObjectMap import *
from Util.ParsePageObjectRepository import *

class LoginPage(object):

    def __init__(self,driver):
        self.driver=driver
        self.parse_config_file=ParserPageObjectRepository()
        self.login_page_items=self.parse_config_file.getItemsFromSection(
            "126mail_login")
        # print self.login_page_items

    def frame(self):
        locateType, locateExpression = self.login_page_items['login_page.frame'].split(">")
        # print locateType, locateExpression
        return getElement(self.driver, locateType, locateExpression)

    def username(self):
        locateType,locateExpression=self.login_page_items['login_page.username'].split(">")
        # print locateType, locateExpression
        return getElement(self.driver, locateType,locateExpression)

    def password(self):
        locateType,locateExpression=self.login_page_items['login_page.password'].split(">")
        # print locateType, locateExpression
        return getElement(self.driver, locateType,locateExpression)

    def loginbutton(self):
        locateType,locateExpression=self.login_page_items['login_page.loginbutton'].split(">")
        # print locateType, locateExpression
        return getElement(self.driver, locateType,locateExpression)

if __name__=="__main__":
    from selenium import webdriver