# coding:utf-8
import url_manager
import html_downloader
import html_paser


class SpiderAnswer(object):

    def __init__(self):

        self.urls = url_manager.UrlManager()
        self.downloader = html_downloader.HtmlDownLoader()
        self.paser = html_paser.HtmlPaser()

    def creaw(self):
        url_list = self.urls.getQuestionUrls()
        for row in url_list:
            link_id = str(row[0])
            root_url = 'http://www.zhihu.com/question/' + link_id
            print root_url
            url_data = self.downloader.download(root_url)
            data = self.paser.getQuestionInfo(link_id, url_data)
            break
        self.paser.db.close()


if __name__ == "__main__":
    obj_spider = SpiderAnswer()
    obj_spider.creaw()
