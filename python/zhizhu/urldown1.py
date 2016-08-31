#!/usr/bin/python
# -*- coding:utf-8 -*-
#urldown.py
import urllib2,cookielib
url = "http://www.lvluole.name/?p=314"
print "最简单的方式"
response = urllib2.urlopen('http://www.lvluole.name/?p=314')
#获取状态码判断是否请求成功
#print response.getcode()
cont = response.read()
print len(cont)

print "加一些参数的方式"
request = urllib2.Request(url)
request.add_header("user-agent","Mozilla/5.0")
response2 = urllib2.urlopen(request)
print response.getcode()

print "添加cookie"

cj = cookielib.CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
urllib2.install_opener(opener)
response3 = urllib2.urlopen(url)
print cj
print len(response3.read())
