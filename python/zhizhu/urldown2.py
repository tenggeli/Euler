# coding:utf-8
import urllib2
from bs4 import BeautifulSoup
url = "http://www.lvluole.name/?p=314"
respon = urllib2.urlopen(url)
conn = respon.read()

souce = BeautifulSoup(conn,'html.parser',from_encoding="utf-8")

print "获取所有链接"

links = souce.find_all('a')
print links
for link in links:
	print link.name,link.get_text(),link.get('href')
