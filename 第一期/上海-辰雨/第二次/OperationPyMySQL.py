#!/usr/bin/env python
# encoding: utf-8
import pymysql
import random
'''
pymysql库进行MySQL的管理操作：
1.Counnection
代表一个与MySQL Server的socket连接，使用connect方法来创建一个连接实例
2.Cursor
代表一个与MySQL数据库交互对象，使用Connection.Cursor()在当前socket连接上的交互对象。
常用API：
Connection 对象常用的API:
connect()	创建一个数据库连接实例
begin()		开始一个事务
close()		发送一个退出消息，并关闭连接
commit()	提交修改至数据库
cursor()	创建一个cursor(游标)实例
ping()		检测服务器是否在运行
rollback()	回滚当前事务
select_db(db)设置当前db
show_warning()显示警告信息
Cursor对象常用的API：
close()		关闭当前cursor
execute()	执行一个sql语句
executemany()批量执行sql语句
fetchall()	取所有数据
fetchone()	取一条数据
'''
if __name__=='__main__':
	print ('PyMySQL基本示例')

	#创建一个连接实例
	conn = pymysql.connect(
		host = 'localhost',#mysql 服务器IP地址，若服务在本机使用localhost
		port = 3306,
		user = 'root',
		password = '',
		db = 'exercise'
	)
	try:
		#创建用于交互的cursor对象
		cursor = conn.cursor()
		#构建插入数据的sql
		sql = "INSERT INTO user (name,password) VALUES (%s,%s)"
		#生成十条测试数据
		sql_data = []
		for index in range(0,10):
			name = 'zhangsi%d'%(random.randint(1,10000))
			pwd_list = []
			for i in range(6):
				pwd_list.append(str(random.randint(0, 9)))
			password = ''.join(pwd_list)
			sql_data.append((name,password))
		print sql_data

		#执行sql语句，进行批量插入数据
		cursor.executemany(sql,sql_data)

		#提交至数据库
		conn.commit()

		#查询5条数据
		sql = "SELECT * FROM user limit 5"

		#执行sql
		cursor.execute(sql)

		#取查询到的所有数据
		all_data = cursor.fetchall()

		#遍历打印出来
		print ('取所有查询到的数据')
		for data in all_data:
			print ("id:%d name:%s password %s"%(data[0],data[1],data[2]))

		#取1条数据
		#cursor.execute(sql)
		one_data = cursor.fetchone()
		print ('\n取1条数据')
		print ("id:%d name:%s password %s" % (data[0], data[1], data[2]))
	finally:
		#最后把数据库连接关闭
		conn.close()
