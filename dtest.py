#coding=utf-8
import ConfigParser

cf=ConfigParser.ConfigParser()
cf.read('C:\Users\Administrator\PycharmProjects\DataDrive\conf\PageElementLocator.ini')
# print cf.sections()
print cf.options('126mail_login')
print cf.get('126mail_login','loginpage.frame')
print dict(cf.items('126mail_login'))
print cf.items('126mail_login')
