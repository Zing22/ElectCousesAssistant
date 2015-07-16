# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup

class ProData(object):
	"""process responce from url,output a list of data"""
	def findTrs(self,tr):
		try:
			#print tr["class"]
			return tr["class"] == [u'odd', u'conflict'] or tr["class"] == [u'even', u'conflict'] or tr["class"] == [u'odd',] or tr["class"] == [u'even',]
		except:
			return False

	def getDataList(self,responce):
		divlist = []
		soup = BeautifulSoup(responce.read(),"html.parser")
		#print soup.prettify()
		for div in soup.find_all(class_="grid-container"):
			divlist.append(div)
			print "in processData.py append one div into list"
		if len(divlist)==0 :
			print "bs4 error"
			return None
		hadList = []
		hadNum = 0
		for tr in divlist[0].find_all(self.findTrs):
			hadList.append(dict())
			#找到名字
			hadList[hadNum]["name"] = tr.find(href="javascript:void(0)").string
			#获取td列表
			tdlist = tr.find_all(class_="c")
			#课程号码
			hadList[hadNum]["number"] = tdlist[0].a["jxbh"]
			#老师
			hadList[hadNum]["teacher"] = tdlist[1].string
			#学分
			hadList[hadNum]["credit_point"] = tdlist[2].string
			#课容量
			hadList[hadNum]["contain"] = tdlist[3].string
			#待筛选
			hadList[hadNum]["waiting"] = tdlist[4].string
			#空位
			hadList[hadNum]["free"] = tdlist[5].string
			#选中率
			hadList[hadNum]["percent"] = tdlist[6].string
			#开课单位
			hadList[hadNum]["college"] = tdlist[7].string
			#校区
			hadList[hadNum]["campus"] = tdlist[8].string.strip()
			#考试方式
			hadList[hadNum]["exammode"] = tdlist[9].string
			#筛选方式
			hadList[hadNum]["filtermode"] = tdlist[10].string
			for key in hadList[hadNum].keys():
				if not hadList[hadNum][key]:
					hadList[hadNum][key] = "N/A"
			hadNum += 1

		waitingList = []
		waitingNum = 0
		for tr in divlist[1].find_all(self.findTrs):
			waitingList.append(dict())
			#找到名字
			waitingList[waitingNum]["name"] = tr.find(href="javascript:void(0)").string
			#是否冲突
			if tr.has_attr("class") and ("conflict" in tr["class"]):
				waitingList[waitingNum]["conflict"] = "Yes"
			else:
				waitingList[waitingNum]["conflict"] = "No"
			#获取td列表
			tdlist = tr.find_all(class_="c")
			#课程号码
			waitingList[waitingNum]["number"] = tdlist[0].a["jxbh"]
			#老师
			waitingList[waitingNum]["teacher"] = tdlist[1].string
			#学分
			waitingList[waitingNum]["credit_point"] = tdlist[2].string
			#课容量
			waitingList[waitingNum]["contain"] = tdlist[3].string
			#待筛选
			waitingList[waitingNum]["waiting"] = tdlist[4].string
			#空位
			waitingList[waitingNum]["free"] = tdlist[5].string
			#选中率
			waitingList[waitingNum]["percent"] = tdlist[6].string
			#开课单位
			waitingList[waitingNum]["college"] = tdlist[7].string
			#校区
			waitingList[waitingNum]["campus"] = tdlist[8].string.strip()
			#考试方式
			waitingList[waitingNum]["exammode"] = tdlist[9].string
			#筛选方式
			waitingList[waitingNum]["filtermode"] = tdlist[10].string
			for key in waitingList[waitingNum].keys():
				if not waitingList[waitingNum][key]:
					print key
					waitingList[waitingNum][key] = "N/A"
			waitingNum += 1
		return waitingList

if __name__ == "__main__":
	f = open('zx.html','r')
	pro = ProData()
	pro.getDataList(f)
	f.close()