# coding:utf-8
import ConfigParser
import pymysql as MySQLdb


class HtmlOutput(object):

    def __init__(self):

        cf = ConfigParser.ConfigParser()
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
        self.datas = []

    def collect_data(self, data):
        if data is None:
            return
        self.datas.append(data)

    def output_html(self):
        # code
