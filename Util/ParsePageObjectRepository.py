#coding=utf-8
from ConfigParser import ConfigParser
from ProjectVar import var

class ParserPageObjectRepository(object):
	def __init__(self):
		self.cf=ConfigParser()
		self.cf.read(var.page_object_path)

	def getItemsFromSection(self, sectionName):
		items = self.cf.items(sectionName)
		return dict(items)


	def getOptionValue(self, sectionName, optionName):
		return self.cf.get(sectionName, optionName)


if __name__ == "__main__":
	pp = ParserPageObjectRepository()
	print pp.getItemsFromSection("126mail_login")
	print pp.getOptionValue("126mail_login", "loginPage.username")
