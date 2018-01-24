import pymysql
import random
__author__='棒棒糖'
if __name__=='__main__':
    print('mysql例子')
    #创建一个连接示例
    con=pymysql.connect(
        host='10.68.3.88', #mysql服务ip地址
        port=3306,#端口
        user='liyiming',
        password='liyiming',
        db='zzb_pro',#默认连接到的数据库
        charset='utf8'#连接字符集
    )

    try:
        #创建用于交互的cursor对象
        cursor=conn.cursor()
        #插入10条测试数据
        #sql语句
        sql="insert into 'users'('email,''password')values(%s,%s)"
        #生成10条数据
        sql_data=[]
        for index in range(0,10):
            email='%.10f@126.com'%random.random()
            password=random.random()
            sql_data.append((email,password))

        #执行sql
        cousor.executemany(sql,sql_data)
        #提交至数据库
        conn.commit()
        #查询数据
        sql="select * from 'users'limit 5"
        #执行sql
        cursor.execute(sql)
        #取查询到的所有数据
        all_data=cursor.fetchall()
        #遍历打印
        print('取所有查询到的数据')
        for data in all_data:
            print('id:%d email:%s password:%s'%(data[0],data[1],data[2]))

        # 取1条数据
        one_data=cursor.fetchone()
        print('\n取1条数据')
        print('id:%d email:%s password:%s'%(one_data[0],one_data[1],one_data[2]))

    finally:
        conn.close()