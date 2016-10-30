# coding:utf-8
import url_manager
import html_downloader
import html_paser
import html_output


class SpiderMain(object):

    def __init__(self):

        self.urls = url_manager.UrlManager()
        self.downloader = html_downloader.HtmlDownLoader()
        self.paser = html_paser.HtmlPaser()
        self.output = html_output.HtmlOutput()

    def creaw(self, root_url):

        html_cont = self.downloader.download(root_url)
        new_data = self.paser.parse(root_url, html_cont)
        print new_data


if __name__ == "__main__":
    root_url = "https://www.zhihu.com/people/teng-ge-li"
    obj_spider = SpiderMain()
    obj_spider.creaw(root_url)
