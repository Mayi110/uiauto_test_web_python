#encoding=utf-8
from selenium import webdriver
from Util.log import *
from Util.FormatTime import *
import time
from PageObject.login_page import *
from PageObject.home_page import *
def login(driver,username, password):

    driver.get("http://mail.126.com")
    time.sleep(2)
    lp = LoginPage(driver)
    driver.switch_to.frame(lp.frame())
    time.sleep(2)
    lp.username().send_keys(username)
    lp.password().send_keys(password)
    lp.loginbutton().click()
    time.sleep(4)
    info("login successfully!")
    # print date_time_chinese()

if __name__=="__main__":
    driver = webdriver.Chrome(executable_path="e:\\chromedriver")
    login(driver,"testman1980", "wulaoshi1978")
