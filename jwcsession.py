# http://202.207.247.49/loginAction.do
#coding=UTF-8
import urllib
import urllib2
import json
import cookielib
import re
import requests
dalidateCodeUrl="http://202.207.247.49/validateCodeAction.do"
loginUrl="http://202.207.247.49/loginAction.do"
headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.6',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Host': '202.207.247.49',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.111 Safari/537.36'
}
def downValidateCode():

    req = urllib2.urlopen(dalidateCodeUrl)
    content = req.read()
    f=open('./validate/'+'validate'+'.jpg','w+')
    f.write(content)
    print '验证码下载完成'

print "请输入学号"
xh=raw_input()
print "请输入密码"
mm=raw_input()
downValidateCode()
print "请输入验证码"
validate=raw_input()
datas = {
    'zjh':xh,
    'mm':mm,
    'v_yzm': validate
}
try:
    s=requests.Session()
    Post=s.post(loginUrl,headers=headers,data=datas)
    print Post.status_codes




except urllib2.HTTPError, e:
    print e.getcode()
    print e.reason
