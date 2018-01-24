# -*-coding:utf-8 -*-

import pymysql
import random

__author__ = "huohuo"

if __name__ == "__main__":
    print("PyMySQL基本示例")

    # 创建一个连接示例
    conn = pymysql.connect(
        host = "",
        port = 3306,
        user = "",
        password = "",
        db = "",
        charset = "utf-8"
    )

    try:
        # 创建用于交互的对象
        cursor = conn.cursor()

        # 构建插入数据的sql
        sql = "INSERT INTO 'users' ('email', 'password') VALUES (%s, %s)"

        # 插入10条数据
        sql_data = []
        for index in range(0, 10):
            email = "%.10f@126.com" % random.random()
            password = random.random()
            sql_data.append((email, password))

        # 执行sql
        cursor.executemany(sql, sql_data)

        # 提交至数据库
        conn.commit()  

        # 查询数据
        sql = "SELECT * FROM 'users' LIMIT 5"

        # 执行sql
        cursor.execute(sql)

        # 取查询到的数据
        all_data = cursor.fetchall()

        # 遍历打印
        print("取所有查询的数据")
        for data in all_data:
            print("id: %d email: %s password: %s" % (data[0], data[1], data[2]))

        # 取一条数据并打印
        one_data = cursor.fetchone()
        print("取一条数据")
        print("id: %d email: %s password: %s" % (one_data[0], one_data[1], one_data[2]))

    finally:
        conn.close()