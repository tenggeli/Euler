# coding:utf-8
import url_manager
import html_downloader
import html_paser
import json

class SpiderMain(object):

    def __init__(self):

        self.urls = url_manager.UrlManager()
        self.downloader = html_downloader.HtmlDownLoader()
        self.paser = html_paser.HtmlPaser()

    def creaw(self, root_url):
        html_cont = self.downloader.download(root_url)
        fout = open('out.json','wb+')
        fout.write(html_cont)
        fout.close()
        with open('out.json') as json_file:
            data = json.load(json_file)

        print (data['paging']['next'])



        # new_data = self.paser.parse(root_url, html_cont)


if __name__ == "__main__":
    root_url = "https://www.zhihu.com/api/v4/members/teng-ge-li/activities"
    obj_spider = SpiderMain()
    obj_spider.creaw(root_url)
