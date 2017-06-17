#coding=utf-8
import logging
import logging.config
import os
from ProjectVar import var

# 读取配置文件
logging.config.fileConfig(var.log_config_path)
# 选择日志格式
logger=logging.getLogger('example02')

def error(message):
	# 打印debug信息
	logger.error(message)

def info(message):
	# 打印info日志信息
	logger.info(message)

def warning(message):
	# 打印warning信息
	logger.warn(message)

if __name__=="__main__":
	print file_path
	info('info')
	error('error')
	warning('warning')