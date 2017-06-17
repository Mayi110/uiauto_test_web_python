#coding=utf-8
import os

#获取当前工程目录
project_path=os.path.dirname(os.path.dirname(__file__))
log_config_path=os.path.join(project_path,'conf','Logger.conf')
page_object_path=os.path.join(project_path,'conf','PageElementLocator.ini')
test_data_excel_path=os.path.join(project_path,'TestData',u'126邮箱联系人.xlsx')
username_col_no=1
password_col_no=2
test_result_col_no=6
test_result_col_no1=10
execute_time_col_no=9
is_execute_col_no=4
is_execute_col_no1=7

if __name__=="__main__":
	print __file__
	print project_path