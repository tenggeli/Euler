# coding:utf-8
import url_manager
import html_downloader
import html_paser


class SpiderQuesion(object):

    def __init__(self):

        self.urls = url_manager.UrlManager()
        self.downloader = html_downloader.HtmlDownLoader()
        self.paser = html_paser.HtmlPaser()

    def creaw(self):
        url_list = self.urls.getUrls()
        for row in url_list:
            link_id = str(row[0])
            print link_id
            root_url = 'http://www.zhihu.com/topic/' + link_id
            fast_url = 'http://www.zhihu.com/topic/' + link_id + '/hot'
            url_data = self.downloader.getHtml(root_url)
            data = self.paser.getTopicsInfo(link_id, url_data)
            url_post_data = self.downloader.download(fast_url)
            question = self.paser.getQuestion(link_id, url_post_data)
        self.paser.db.close()

if __name__ == "__main__":
    obj_spider = SpiderQuesion()
    obj_spider.creaw()
