# coding:utf-8
from bs4 import BeautifulSoup
import re
import configparser
import pymysql as MySQLdb


class HtmlPaser(object):
    def __init__(self):
        self.data = {}
        self.fast_data = {}
        self.img_data = set()
        cf = configparser.ConfigParser()
        cf.read("config.ini")
        host = cf.get("db", "host")
        port = int(cf.get("db", "port"))
        user = cf.get("db", "user")
        passwd = cf.get("db", "passwd")
        db_name = cf.get("db", "db")
        charset = cf.get("db", "charset")
        use_unicode = cf.get("db", "use_unicode")
        self.db = MySQLdb.connect(
            host=host,
            port=port,
            user=user,
            passwd=passwd,
            db=db_name,
            charset=charset,
            use_unicode=use_unicode
        )
        self.cursor = self.db.cursor()

    def _get_new_urls(self, page_url, soup):
        links = soup.find_all(class_=re.compile("zm-profile-section-item"))
        tmp = False
        for link in links:
            url_tmp = link.find('a', href=re.compile(r"/\w+/\d"))
            url = url_tmp['href']
            topics_name = link.find('strong')
            url_id = url.split("/")
            src = link.find('img').get('src')
            self.data = {
                'topics_photo' : src,
                'topics_id' : url_id[-1],
                'topics_name':topics_name.get_text()
            }
            tmp = self._save_data_topic(self.data)
        return tmp

    def _save_data_topic(self, data):
        try:
            self.cursor.execute("""REPLACE into topics(topics_id,topics_name,topics_photo)
            values (%s, %s,%s)""", (
                self.data['topics_id'],
                self.data['topics_name'],
                self.data['topics_photo'])
            )
            self.db.commit()
        except MySQLdb.Error:
            print ("Mysql Error %d: %s" % MySQLdb.Error)
            self.db.rollback()

        return True

    def parse(self, page_url, html_cont):
        if page_url is None or html_cont is None:
            return

        soup = BeautifulSoup(html_cont, 'html.parser', from_encoding='utf-8')
        new_urls = self._get_new_urls(page_url, soup)
        self.db.close()
        return new_urls

    def getTopicsInfo(self, link_id, html_cont):
        if link_id is None or html_cont is None:
            return
        soup = BeautifulSoup(html_cont, 'html.parser', from_encoding='utf-8')
        links = soup.find_all(class_=re.compile("feed-content"))
        topic_info_tmp = soup.find(class_=re.compile("zu-main-sidebar"))
        topic_info_t = topic_info_tmp.find(class_=re.compile('zm-editable-content'))

        if topic_info_t is None:
            topic_info = ''
        else:
            topic_info = topic_info_t.get_text()

        topic_num_tmp = soup.find(class_=re.compile('zm-topic-side-followers-info'))
        topic_num = topic_num_tmp.find('strong').get_text()
        self.fast_data = {
                'topics_info':topic_info,
                'topics_num':topic_num,
            }
        self._update_topics_data(self.fast_data, link_id)

    def getQuestion(self, link_id, html_cont):
        if link_id is None or html_cont is None:
            return
        soup = BeautifulSoup(html_cont, 'html.parser', from_encoding='utf-8')
        links = soup.find_all('a',class_=re.compile("question_link"))
        for link in links:
            url = link['href']
            url_id = url.split("/")
            self.data = {
                'question_id' : url_id[-1],
                'question_name' :link.get_text(),
                'topics_id':link_id,
            }
            self._save_question_data(self.data)

    def getQuestionInfo(self, link_id, html_cont):
        if link_id is None or html_cont is None:
            return
        soup = BeautifulSoup(html_cont, 'html.parser', from_encoding='utf-8')
        question_info = soup.find('div', id=re.compile('zh-question-detail')).get_text()
        question_flows_tmp = soup.find('div', class_=re.compile('zg-gray-normal'))
        question_flows = question_flows_tmp.find('strong').get_text()
        question_num_tmp = soup.find('div', class_=re.compile('zh-answers-title'))
        question_num = question_num_tmp.find('h3')
        self.fast_data = {
                'question_num':question_num['data-num'],
                'question_info':question_info,
                'question_flow':question_flows,
        }
        self._update_question_data(self.fast_data, link_id)
        self.getAnswerData(link_id, html_cont)

    def getAnswerData(self, link_id, html_cont):
        if link_id is None or html_cont is None:
            return
        soup = BeautifulSoup(html_cont, 'html.parser', from_encoding='utf-8')
        print (soup)
        links = soup.find_all('div', class_=re.compile("zm-item-answer"))
        for link in links:
            text = link.find('div', class_=re.compile('js-collapse-body'))
            """
            agree_with_num = link.find('div', class_=re.compile('zm-item-vote-info'))
            answer_person_id = link.find('a', class_=re.compile('author-link'))
            imgs = link.find('img', class_=re.compile('zm-list-avatar'))
            url = answer_person_id['href']
            url_id = url.split("/")
            self.data = {
                'question_id':link_id,
                'answer_id':1222,
                'answer_data':text,
                'agree_with_num':agree_with_num['data-votecount'],
                'answer_person_id':url_id[-1],
                'answer_person_photo':imgs['src'],
            }
            # self._save_answer_data(self.data)
            """

    def _save_question_data(self, data):
        try:
            self.cursor.execute("""REPLACE into question(topics_id,question_id,question_name)
            values (%s, %s,%s)""", (
                self.data['topics_id'],
                self.data['question_id'],
                self.data['question_name'])
            )
            self.db.commit()
        except MySQLdb.Error:
            print ("Mysql Error %d: %s" % MySQLdb.Error)
            self.db.rollback()

    def _save_answer_data(self, data):
        try:
            self.cursor.execute("""REPLACE into answer(question_id,
                answer_id,answer_data,agree_with_num,
                answer_person_id,answer_person_photo)
            values (%s, %s,%s,%s,%s,%s)""", (
                self.data['question_id'],
                self.data['answer_id'],
                self.data['answer_data'],
                self.data['agree_with_num'],
                self.data['answer_person_id'],
                self.data['answer_person_photo'])
            )
            self.db.commit()
        except MySQLdb.Error:
            print ("Mysql Error %d: %s" % MySQLdb.Error)
            self.db.rollback()

    def _update_topics_data(self, data, topics_id):
        try:
            self.cursor.execute("""UPDATE topics set topics_num = %s,
                topics_info = %s where topics_id = %s""", (
                data['topics_num'],
                data['topics_info'],
                topics_id)
            )
            self.db.commit()
        except MySQLdb.Error:
            print ("Mysql Error %d: %s" % MySQLdb.Error)
            self.db.rollback()

    def _update_question_data(self, data, topics_id):
        try:
            self.cursor.execute("""UPDATE question set question_num = %s,
                question_info = %s,question_flow =%s where question_id = %s""",
                (
                    data['question_num'],
                    data['question_info'],
                    data['question_flow'],
                    topics_id)
                )
            self.db.commit()
        except MySQLdb.Error:
            print ("Mysql Error %d: %s" % MySQLdb.Error)
            self.db.rollback()
