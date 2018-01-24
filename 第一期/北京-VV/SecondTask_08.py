# -*- coding:utf-8 -*-

__author__ = 'VV'

'''
import smtplib
from email.mime.text import MIMEText
from email.header import Header

if __name__ == '__main__':
    print("send text email demo")

    # sender
    sender = "deep_test@126.com"

    # receiver
    receivers = "110211880@qq.com"

    # send content
    # text type
    msg = MIMEText("uku:ukulele", "hello", "utf-8")
    msg["From"] = "deep_test@126.com"
    msg["To"] = receivers

    # create email title
    msg["Subject"] = Header("Ukulele_fan", "utf-8")

    # smtp server
    smtpserver = "smtp.126.com"
    smtpport = 25

    # username
    username = "deep_test"

    # pw
    password = "123456a"

    # create smtp object
    smtp = smtplib.SMTP()

    # connect to smtp server
    con = smtp.connect(smtpserver, smtpport)
    print("Connection result: ", con)

    # login smtp server
    log = smtp.login(username, password)
    print("Login result: ", log)

    # send email
    print(receivers)
    res = smtp.sendmail(sender, receivers, msg.as_string())
    print("Email send result: ", res)

    # Quit
    smtp.quit()
    print("send email finish")
'''

'''
import smtplib

from email.mime.text import MIMEText
from email.header import Header

if __name__ == '__main__':
    print("send HTML email demo")

    # sender
    sender = "deep_test@126.com"

    # receiver
    receivers = "110211880@qq.com"

    # create email content
    # html type
    msg = MIMEText("<P>Uku:ukulel</p><a href='http:///www.baidu.com'>Baidu</a>",
        "html",
        "utf-8")
    msg["From"] = "deep_test@126.com"
    msg["To"] = receivers

    # create email title
    msg["Subject"] = Header("Ukulele_fan", "utf-8")

    # smtp server
    smtpserver = "smtp.126.com"
    smtpport = 25

    # username
    username = "deep_test"

    # pw
    password = "123456a"

    # create smtp object
    smtp = smtplib.SMTP()

    # connect to smtp server
    con = smtp.connect(smtpserver, smtpport)
    print("Connection result: ", con)

    # login smtp server
    log = smtp.login(username, password)
    print("Login result: ", log)

    # send email
    print(receivers)
    res = smtp.sendmail(sender, receivers, msg.as_string())
    print("Email send result: ", res)

    # Quit
    smtp.quit()
    print("send email finish")

'''

'''
import smtplib

from email.mime.text import MIMEText
from email.header import Header
from email.mime.multipart import MIMEMultipart

if __name__ == '__main__':
    print("Send HTML with attachment demo")

    # sender
    sender = "deep_test@126.com"

    # receiver
    receivers = "110211880@qq.com"

    # create email content
    # html type
    msg = MIMEMultipart()

    msg["From"] = "deep_test@126.com"
    msg["To"] = receivers

    # create email title
    msg["Subject"] = Header("Ukulele_fan", "utf-8")

    # create email text
    msg.attach(MIMEText("Uku: Ukulele", "Hello", "utf-8"))

    # create attachment
    attach1 = MIMEText(open("test.py", "rb").read(), "base64", "utf-8")
    attach1["Content-Type"] = "application/octet-stream"

    # display the filename in the Email
    attach1["Content-disposition"] = "attachment;filename=code.py"

    # link attachment to email
    msg.attach(attach1)

    # smtp server
    smtpserver = "smtp.126.com"
    smtpport = 25

    # username
    username = "deep_test"

    # pw
    password = "123456a"

    # create smtp object
    smtp = smtplib.SMTP()

    # connect to smtp server
    con = smtp.connect(smtpserver, smtpport)
    print("Connection result: ", con)

    # login smtp server
    log = smtp.login(username, password)
    print("Login result: ", log)

    # send email
    print(receivers)
    res = smtp.sendmail(sender, receivers, msg.as_string())
    print("Email send result: ", res)

    # Quit
    smtp.quit()
    print("send email finish")
'''

import pymysql
import random

if __name__ == '__main__':
    print("PyMySQL demo")

    # create a connect instance
    conn = pymysql.connect(
        host="localhost", # mysql server ip address, also can use localhost
        port=3306, # mysql server port
        user="root", # access mysql server username
        password="123123", # pw
        db="test_py", # default connect database
        charset="utf8"
    )

    try:
        # create cursor
        cursor = conn.cursor()

        # insert 10 test data
        # create sql of insert data
        sql = "INSERT INTO `users` (`email`, `password`) VALUES (%s, %s)"

        # 10 test data
        sql_data = []
        for index in range(0, 10):
            email = f"{random.random()}.10f@126.com"
            password = random.random()
            sql_data.append((email, password))

        # run sql, batch insert data
        cursor.executemany(sql, sql_data)

        # commit to db
        conn.commit()

        # check 5 datas
        sql = "SELECT * FROM `users` LIMIT 5"

        # run sql
        cursor.execute(sql)

        # select all data
        all_data = cursor.fetchall()

        # traverse print
        print(type(all_data))
        print("all data")
        for data in all_data:
            print(f"email: {data[0]} password: {data[1]}")

        # get 1 data
        cursor.execute(sql)
        one_data = cursor.fetchone()
        print(type(one_data))
        print("\n Get 1 data")
        print(f"email: {one_data[0]} password: {one_data[1]}")

    finally:
        # close db
        conn.close()
