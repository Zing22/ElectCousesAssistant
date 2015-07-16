#-*- coding:utf-8 -*-

from login import Login
import urllib,urllib2
import cookielib
import Image
import time
from bs4 import BeautifulSoup
from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import pyqtSignal

default_delay_time = 7

class SummitReq(QtCore.QObject):
    """docstring for SummitReq"""
    sSignal = pyqtSignal(str)
    exitSign = pyqtSignal()
    times = pyqtSignal()
    def __init__(self, lo):
        super(SummitReq, self).__init__()
        self.sid = lo.sid
        self.jid = lo.jid
        self.secs = default_delay_time
        self.opener = lo.opener
        self.runFlag = True

    def setSleep(self,secs):
        try:
            self.secs = int(secs)
        except:
            self.secs = default_delay_time
        finally:
            if(self.secs<default_delay_time):
                print u'时间太短！自动调整为%s秒。' % default_delay_time
                self.secs = default_delay_time

    def printLessons(self,lessons):
        for les in lessons:
            if les.has_attr('href'):
                print les.get_text()
        return

    def getPage(self,posturl,header):
        request = urllib2.Request(posturl,None,header)
        try:
            response = self.opener.open(request)
            return response
        except urllib2.URLError,e:
            print "Error reason:", e.reason
            #print "Return content", e.read()
            return False
        except:
        	return False

    def submit(self,LessonIds,kclb=21):
        url = 'http://uems.sysu.edu.cn/elect/s/courses?kclb=%s&xnd=2015-2016&xq=1&fromSearch=false&sid=%s' % (kclb,self.sid)
        #build header
        header = {
            'Host':'uems.sysu.edu.cn',
            'Connection':'keep-alive',
            'Content-Length':'60',
            'Accept':'*/*',
            'Origin':'http://uems.sysu.edu.cn',
            'X-Requested-With':'XMLHttpRequest',
            'User-Agent':'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.130 Safari/537.36',
            'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',
            'Referer':url,
            'Accept-Encoding':'gzip, deflate',
            'Accept-Language':'zh-CN,zh;q=0.8',
            'Cookie': self.jid,

        }
        #build post data
        while self.runFlag and LessonIds :
            print 'LessonIds:',LessonIds
            for LessonId in LessonIds:
            	print 'post:%s' % LessonId
                postData = {
                            'jxbh':LessonId,\
                            'sid': self.sid,\
                            }
                postData = urllib.urlencode(postData)
                posturl = 'http://uems.sysu.edu.cn/elect/s/elect'
                request = urllib2.Request(posturl,postData,header)
                try:
                    response = self.opener.open(request)
                    print 'post successed!'
                except urllib2.URLError,e:
                    print '['+str(e.code)+']',e.reason
                except:
                	print 'other error!'
                url, header = self.bulidCheckHeader(21, 4)
                page = self.getPage(url, header)
                if self.checkPage(LessonId,page):
                    self.sSignal.emit(LessonId)
                    print 'seccess:%s! send sSignal!' % LessonId
                    LessonIds.remove(LessonId)
                time.sleep(1)
            self.times.emit()
            print 'left:%d' % len(LessonIds)
            print u'选课未结束，%s秒后重试...' % self.secs
            print '------'
            time.sleep(self.secs)
        self.exitSign.emit()
        return LessonIds

    def bulidCheckHeader(self, kclb, xq):
        #kclb 21专选 30公选
        #xq 1南校 2北校 3珠海 4东校
        #build header
        params = urllib.urlencode({
                    'kclb':kclb,\
                    'xqm':xq,\
                    'xnd':'2015-2016',\
                    'xq':'1',\
                    'sid':self.sid,\
                    'fromSearch':'false',\
                    })
        url = ('http://uems.sysu.edu.cn/elect/s/courses?%s' % params)

        header = {
                'Host' : 'uems.sysu.edu.cn',\
                'User-Agent' : 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.130 Safari/537.36',\
                'Accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',\
                'Accept-Language' : 'zh-CN,zh;q=0.8',\
                'Accept-Encoding' : 'gzip, deflate, sdch',\
                'Referer' : ('http://uems.sysu.edu.cn/elect/s/type?%s' % self.sid),\
                'Cookie' : self.jid,\
                'Connection' : 'keep-alive',\
                }
        return url,header

    def checkPage(self,LessonId,response):
        soup = BeautifulSoup(response.read(),"html.parser")
        lessons = soup.find(id='elected').find_all('a')
        for item in lessons:
            if item.has_attr('jxbh') and item['jxbh'] == LessonId:
                print u'抢课成功！已选的课程：'
                self.printLessons(lessons)
                return True
        return False

if __name__ == '__main__':
    lo = Login()
    j_code = lo.getCAPTCHA(lo.getCookie())
    Image.open('./image/code.jpg').show()
    j_code = raw_input(r"输入看到的验证码：")
    username = raw_input('username:')
    password = raw_input('password:')
    print lo.getSid(username, password, j_code)
    subm = SummitReq(lo)
    LessonIds = ['35000192151001','35000123151002','35000192151003'\
    			,'35000192151023','35000152151003','35000190151003']
    subm.submit(LessonIds)


