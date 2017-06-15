import urllib2

url='http://www.baidu.com'


res=urllib2.urlopen(url)
print res.read()