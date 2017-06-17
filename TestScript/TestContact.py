#encoding=utf-8
from selenium import webdriver
from Util.log import *
from Util.FormatTime import *
from Util.ParseExcel import *
from ProjectVar.var import *
import time
from Action.visit_address_page import *
from Action.add_contact import *
from Action.login import *
import sys
reload(sys)
sys.setdefaultencoding("utf8")

# 遍历excel文件中的测试数据
pe = ParseExcel(test_data_excel_path)
pe.set_sheet_by_index(0)
info("sheetname: "+pe.get_default_name())
for id,row in enumerate(pe.get_all_rows()[1:],2):
	info("username: " +row[username_col_no].value)
	# info(row[password_col_no].value)
	if row[is_execute_col_no].value.lower()=='y':
		username = row[username_col_no].value
		password = row[password_col_no].value
		driver = webdriver.Chrome(executable_path="D:\software\webdriver\chromedriver")
		try:
			login(driver, username, password)
			visit_address_page(driver)
			# 遍历第二个sheet中的测试数据
			pe.set_sheet_by_index(1)
			info("sheetname: " + pe.get_default_name())
			for id, row in enumerate(pe.get_all_rows()[1:], 2):
				info("add_user: "+ row[username_col_no].value)
				# info(row[password_col_no].value)
				if row[is_execute_col_no1].value.lower() == 'y':
					try:
						time.sleep(1)
						add_contact(driver,row[1].value,row[2].value,True,row[4].value,row[5].value)
						pe.write_cell_content(id, execute_time_col_no, date_time_chinese())
						pe.write_cell_content(id, test_result_col_no1, 'pass')

					except Exception, e:
						print e.message
						pe.write_cell_content(id, execute_time_col_no, date_time_chinese())
						pe.write_cell_content(id, test_result_col_no1, 'fail')
				else:
					info('test skip-->'+row[username_col_no].value)
					continue
			time.sleep(3)
			# row[test_result_col_no].value='pass'
			# pe.save_excel_file()
			pe.write_cell_content(id,test_result_col_no,'pass')
		except Exception,e:
			info(e.message)
			pe.write_cell_content(id,test_result_col_no,'fail')
		finally:
			info('quit browser...')
			driver.quit()
	else:
		info('skip-->' + row[username_col_no].value)
		continue
