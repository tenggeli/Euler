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
        count = 1
        self.urls.add_new_url(root_url)
        while self.urls.has_new_url():
            try:
                new_url = self.urls.get_new_url()
                print 'craw %d:%s' % (count, new_url)
                html_cont = self.downloader.download(new_url)
                new_urls, new_data = self.paser.parse(new_url, html_cont)
                self.urls.add_new_urls(new_urls)
                self.output.collect_data(new_data)
                if count == 1000:
                    break

                count = count + 1
            except:
                print 'creaw fail'

        self.output.output_html()


if __name__ == "__main__":
    root_url = "http://baike.baidu.com/view/21087.htm"
    obj_spider = SpiderMain()
    obj_spider.creaw(root_url)
