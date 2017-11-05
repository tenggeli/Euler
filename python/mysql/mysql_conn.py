# codeing:utf-8
import MySQLdb

conn = MySQLdb.Connect(
	host	='127.0.0.1',
	port    =3306,
	user 	='root',
	passwd  ='qufenqi',
	db = 'test',
	charset ='utf8',
	)

cursor = conn.cursor()
sql = 'select * from test_python'
cursor.execute(sql)

print cursor.rowcount()

# execute
cursor.close()
conn.close()
