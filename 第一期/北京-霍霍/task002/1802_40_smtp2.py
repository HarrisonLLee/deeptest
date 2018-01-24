# -*- coding:utf-8 -*-
__author__ = "huohuo"

import smtplib
from email.mime.text import MIMEText
from email.header import Header

if __name__ == "__main__":
    print("发送HTML邮件示例")

    # 邮件发送者
    sender = "q15110185703@126.com"

    receivers = "814235710@qq.com"

    msg = MIMEText("<p>微信公众号：开源优测</p><a href='http://www.testingunion.com'>开源优测社区", "html", "utf-8")
    msg["From"] = "q15110185703@126.com"
    msg["To"] = receivers

    # 构建邮件标题
    msg["Subject"] = Header("开源优测", "utf-8")

    # smtp服务
    smtpserver = "smtp.126.com"
    smtpport = 25

    # 发件人账号
    username = "q15110185703"
    password = "deeptest123"

    # 构建smtp对象
    smtp = smtplib.SMTP()

    # 连接到smtp服务
    con = smtp.connect(smtpserver, smtpport)
    print("连接结果：", con)

    # 登录smtp服务
    log = smtp.login(username, password)
    print("登录结果：", log)

    # 发送邮件
    print(receivers)
    res = smtp.sendmail(sender, receivers, msg.as_string())
    print("发送结果：", res)

    # 退出
    smtp.quit()
    print("send email finish")

