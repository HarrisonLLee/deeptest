# -*- coding:utf-8 -*-
__author__ = "huohuo"

import smtplib
from email.mime.text import MIMEText
from email.header import Header
from email.mime.multipart import MIMEMultipart

if __name__ == "__main__":
    print("发送带附件邮件示例")
    # 邮件发送者
    sender = "q15110185703@126.com"
    receivers = "814235710@qq.com"

    msg = MIMEMultipart()
    msg["From"] = "q15110185703@126.com"
    msg["To"] = receivers

    msg["Subject"] = Header("开源优测", "utf-8")

    # 构造邮件正文
    msg.attach(MIMEText("微信公众号", "plain", "utf-8"))

    # 构造附件
    attch1 = MIMEText(open("1802_40_smtp2.py", 'rb').read(), "base64", "utf-8")
    attch1["Content-Disposition"] = "attrachment;filename=code.py"

    # 关联附件到邮件中
    msg.attach(attch1)

    # smtp服务
    smtpserver = "smtp.126.com"
    smtpport = 25

    # 发件人信息
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

    res = smtp.sendmail(sender, receivers, msg.as_string())
    print("发送结果：", res)

    smtp.quit()
    print("send email finish")

