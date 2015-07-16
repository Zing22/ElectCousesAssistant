#-*- coding:utf-8 -*-

import urllib,urllib2
import cookielib
import Image
import socket

class Login(object):
	"""save sid and cookie"""
	def __init__(self):
		super(Login, self).__init__()
		print r"初始化中..."
		self.sid = ''
		self.jid = ''
		self.errorMeg = ''

	def getCookie(self):
		ck = cookielib.CookieJar()
		self.opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(ck))
		try:
			self.opener.open('http://uems.sysu.edu.cn/elect')
		except urllib2.URLError,e:
			print "Error reason:", e.reason
			#print "Return content:\n", e.read()
			return None
		for item in ck:
			self.jid = item.name+'='+item.value
			return self.jid
		return None

	def getCAPTCHA(self, cookie):
		print self.jid
		header = {
			'Accept':'image/webp,*/*;q=0.8',\
			'Accept-Encoding':'gzip, deflate, sdch',\
			'Accept-Language':'zh-CN,zh;q=0.8',\
			'Connection':'keep-alive',
			'Cookie':self.jid,\
			'Host':'uems.sysu.edu.cn',\
			'Referer':'http://uems.sysu.edu.cn/elect/',\
			'User-Agent':'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.130 Safari/537.36'}
		params = urllib.urlencode({'v':'0.1932646029163152'})
		capurl = ('http://uems.sysu.edu.cn/elect/login/code?%s' % params)
		try:
			resp = self.opener.open(urllib2.Request(capurl,headers=header))
		except:
			print u"inside - 验证码获取失败！"
			return
		f = file("./image/code.jpg",'wb')
		f.write(resp.read())
		f.close()
		#改变图片大小
		img = Image.open("./image/code.jpg")
		(x,y) = img.size
		newimg = img.resize((121,41,))
		newimg.save("./image/code.jpg")
		return 

	def getSid(self,username,password,j_code):
		if username=='' or password=='' or j_code=='':
			return '','输入不能为空'
		#build header
		header = {
			'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',\
			'Accept-Encoding':'gzip, deflate',\
			'Accept-Language':'zh-CN,zh;q=0.8',\
			'Cache-Control':'max-age=0',\
			'Connection':'keep-alive',\
			'Content-Length':'80',\
			'Content-Type':'application/x-www-form-urlencoded',\
			'Cookie':self.jid,\
			'Host':'uems.sysu.edu.cn',\
			'Origin':'http://uems.sysu.edu.cn',\
			'Referer':'http://uems.sysu.edu.cn/elect/index.html',\
			'User-Agent':'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.130 Safari/537.36',\
			}

		#build post data
		postData = {'username':username,\
				'password':password,\
				'j_code':j_code,\
				'lt':'',\
				'_eventId':'submit',\
				'gateway':'true',\
				}
		postData = urllib.urlencode(postData)
		posturl = 'http://uems.sysu.edu.cn/elect/login'
		request = urllib2.Request(posturl,postData,header)
		print 'post!'
		try:
			resp = self.opener.open(request,timeout = 5)
		except urllib2.URLError,e:
			print "Error reason:", e.reason
			try:
				if e.reason.find('getaddrinfo') != -1:
					return '', u"网络错误"
				if e.read().find(r"验证码") == -1:
					self.errorMeg = u"账号或密码错误"
				elif e.read().find(r"账号"):
					self.errorMeg = u"验证码错误"
				elif e.reason.find('Server') != -1:
					self.errorMeg = u"服务器错误"
				self.sid = ''
				return '' , self.errorMeg
			except:
				return '', u"网络错误"
		except socket.timeout, e:
			print u"请求超时"
			return '' , u"请求超时,检查输入"
		except:
			return '', u"未知错误"
		

		#get sid
		self.errorMeg = ''
		string = str(resp.geturl())
		self.sid = string[string.find(r'sid=')+4:]
		return self.sid, self.errorMeg

if __name__ == '__main__':
	lo = Login()
	j_code = lo.getCAPTCHA(lo.getCookie())
	Image.open('./image/code.jpg').show()
	j_code = raw_input(r"输入看到的验证码：")
	username = raw_input('username:')
	password = raw_input('password:')
	print lo.getSid(username, password, j_code)