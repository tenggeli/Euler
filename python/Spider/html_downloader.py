# coding:utf-8
import urllib3,configparser
import urllib.request
import urllib.parse
import json

class HtmlDownLoader(object):

    def download(self, url):
        if url is None:
            return None
        req = urllib.request.Request(url)
        cf = configparser.ConfigParser()
        cf.read("config.ini")

        req.add_header('Connection', 'keep-alive')
        req.add_header('accept', 'application/json, text/plain, */*')
        req.add_header('x-udid', 'AEBAwryS9AmPTouCwBTehleje9c4zTrD5kY=')
        req.add_header('User-Agent', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36')
        req.add_header('x-api-version', '3.0.40')
        req.add_header('authorization', 'Bearer Mi4wQUFCQWxkY1pBQUFBUUVEQ3ZKTDBDUmNBQUFCaEFsVk5Nc2ZaV0FCMEJEeTBWTzlZWWJBR2pVby1kY3FoSndKNHpR|1488594969|d24837b40731e74a015d07f6815f1e4517ffdb67')
        req.add_header('Referer', 'https://www.zhihu.com/people/teng-ge-li/activities')
        req.add_header('Cache-Control', 'no-cache')

        Request = urllib.request.urlopen(req)
        if Request.getcode() != 200:
            return None
        data = Request.read()
        return data

    def getHtml(self, url):
        if url is None:
            return None

        req = urllib3.Request(url)
        Request = urllib3.urlopen(req)

        if Request.getcode() != 200:
            return None
        data = Request.read()

        return data

    def getPostHtml(self, url):
        if url is None:
            return None

        headers = {
            'user-agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.111 Safari/537.36',
            'referer':'https://www.zhihu.com/topic/19561513/hot',
            'host':'www.zhihu.com','Origin':'http://www.zhihu.com',
            'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',
            'Connection':'keep-alive','X-Requested-With':'XMLHttpRequest','Content-Length':'81',
            'Accept-Encoding':'gzip,deflate','Accept-Language':'zh-CN,zh;q=0.8','Connection':'keep-alive'
        }
