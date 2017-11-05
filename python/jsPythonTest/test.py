# _*_coding:utf8_*_
# douban.py
# 爬取豆瓣小组讨论话题
import time
from lxml import etree
from selenium import webdriver

class PhantomSpider:
    def getContent(self, url):
        browser = webdriver.PhantomJS(executable_path='/usr/local/bin/phantomjs')
        browser.get(url)
        time.sleep(3)
        html = browser.execute_script("return document.documentElement.outerHTML")
        # output = etree.HTML(html)
        return html

url = "https://www.zhihu.com/"
totalpages = 5
doubanSpider = PhantomSpider()
content = doubanSpider.getContent(url)
print(content)
print("爬取开始")
file_obj = open('./zhihu.html', 'w', encoding='UTF-8')
file_obj.write(content)
file_obj.close()
