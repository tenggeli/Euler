# coding:utf-8
import ConfigParser
import pymysql as MySQLdb

class DataInfo(object):

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


if __name__=='__main__':
    info = DataInfo()

    # 建表
    info.create_question_table()
    info.create_people_table()
    info.create_people_merged_table()

    # 等 people 的数据抓取完成，construct_people_db_v2 函数调用之后再调用此方法
    # info.merge_people_of_db()
    info.close_mysql()
