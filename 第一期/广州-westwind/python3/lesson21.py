#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/1/20 17:19
# @Author  : caijiangchun
# @Site    : 
# @File    : lesson21.py
# @Software: PyCharm

import smtplib
from email.mime.text import MIMEText
from email.header import Header


def send_text():
    print("发送文本邮件")

    #邮件发送者
    sender = "caijc99@126.com"

    #邮件接收地址列表
    receivers = "caijc90@163.com"

    #text标志发送的内容为文本格式
    msg = MIMEText("CAI开源", "plain", "utf-8")

    # html标识发送内容为html格式
    # msg = MIMEText("<p>微信公众号号：开源优测</p><a href='http://www.testingunion.com'>开源优测社区</a>>",
    #                "html",
    #                "utf-8")
    msg["From"] = sender
    msg["To"] = receivers

    #构建邮件标题
    msg["Subject"] = Header("开源test", "utf-8")

    #smtp服务
    smtpserver = "smtp.126.com"
    smtpport = 25

    # 发送人邮件用户名或专用于smtp账户用户名
    username = "caijc99@126.com"

    #发送人邮件密码
    password = ""

    # 构建smtp对象
    smtp = smtplib.SMTP()

    #连接到smtp服务
    con = smtp.connect(smtpserver, smtpport)
    print("连接结果： " , con)

    # 登录smtp服务
    log = smtp.login(username, password)
    print("登录结果： ", log)

    # 发送邮件
    res = smtp.sendmail(sender, receivers, msg.as_string())
    print("邮件发送结果：" , res)

    # 退出
    smtp.quit()
    print("send email finish")

if __name__ == "__main__":

    send_text()
