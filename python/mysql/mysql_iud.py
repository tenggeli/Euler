#codeing:utf-8
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
try:
	for i in  range(1,100):
	sel_insert = "insert into test_python (id,name) values (%s,'name%s')" %(i,i)
	cursor.execute(sel_insert)
	print cursor.rowcount

	conn.commit()
except Exception, e:
	print e

	conn.rollback()

# sel_update = "update  test_python  set name ='' where id =1 "

# sel_delect = "delete from test_python where id <2 "


# # execute
cursor.close()
conn.close()
