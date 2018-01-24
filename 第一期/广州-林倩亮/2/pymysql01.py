import pymysql.cursors

# Connect to the datebase
connection = pymysql.connect(
					host='211.149.191.240',
					user='tester',
					password='funfunfun',
					db='py_test',
					charset='utf8mb4',
					cursorclass = pymysql.cursors.DictCursor
)
try:
	with connection.cursor() as cursor:
		#Create a new record
		sql = 'INSERT INTO persons VALUES (3,"国兵","里","潮州","广东");'
		cursor.execute(sql)
	connection.commit()
	
finally:
	connection.close()
	
	
# connect() 建立数据库连接
# execute() 执行SQL语句
# close() 关闭数据库连接