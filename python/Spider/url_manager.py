# coding:utf-8
import configparser
import pymysql


class UrlManager(object):

    def __init__(self):
        self.new_urls = set()
        self.old_urls = set()
        cf = configparser.ConfigParser()
        cf.read("config.ini")
        host = cf.get("db", "host")
        port = int(cf.get("db", "port"))
        user = cf.get("db", "user")
        passwd = cf.get("db", "passwd")
        db_name = cf.get("db", "db")
        charset = cf.get("db", "charset")
        use_unicode = cf.get("db", "use_unicode")
        self.db = pymysql.connect(
            host=host,
            port=port,
            user=user,
            passwd=passwd,
            db=db_name,
            charset=charset,
            use_unicode=use_unicode
        )
        self.cursor = self.db.cursor()

    def getUrls(self):
        p_str = "select topics_id from topics ";
        self.cursor.execute(p_str)
        data = self.cursor.fetchall()
        return data

    def getQuestionUrls(self):
        p_str = "select question_id from question ";
        self.cursor.execute(p_str)
        data = self.cursor.fetchall()
        return data
