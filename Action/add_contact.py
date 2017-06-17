#encoding=utf-8
from selenium import webdriver
from Util.log import *
from Util.FormatTime import *
import time
from PageObject.login_page import *
from PageObject.home_page import *
from PageObject.addressBook import *

def add_contact(driver,name,email='',is_star=True,mobile='',other_info=''):
	ap= AddressPage(driver)
	ap.add_contact_button().click()
	time.sleep(2)
	ap.contact_name().send_keys(name)
	ap.contact_email().send_keys(email)
	if is_star:
		ap.contact_is_star().click()
	ap.contact_mobile().send_keys(mobile)
	ap.contact_other_info().send_keys(other_info)
	ap.contact_save_button().click()


if __name__=="__main__":
    driver = webdriver.Chrome(executable_path="D:\software\webdriver\chromedriver")
    login(driver,"liudongjie2015", "liudongjie126")
    visit_address_page(driver)
    add_contact(driver,'test','rrrr@test.com',True,'15233334444')
    driver.quit()