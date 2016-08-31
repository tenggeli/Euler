#coding:utf-8
import urllib2

class HtmlDownLoader(object):

	def download(self,url):
		if url is None:
			return None

		respose = urllib2.urlopen(url)

		if respose.getcode() != 200:
			return None

		return respose.read()
