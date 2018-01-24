#-*-coding:utf-8
__author__ = "Lakisha"

'''
import smtplib
from email.mime.text import MIMEText
from email.header import Header

if __name__ == "__main__":
    print("发送文本邮件示例")

    #邮件发送者
    sender = "deep_test@126.com"

    #邮件接收地址列表
    receivers = "673250728@qq.com"

    #发送内容构建
    #text表示发送内容为文本格式
    msg = MIMEText("微信公众号：开源优测", "plain", "utf-8")
    msg["From"] = "deep_test@126.com"
    msg["To"] = receivers

    #构建邮件标题
    msg["subject"] = Header("开源优测_DeepTest", "utf-8")

    #SMTP服务
    smtpserver = "smtp.126.com"
    smtpport = 25

    #大送人邮件密码或专用于SMTP账户用户名
    username = "deep_test"

    #发送人邮件密码或专用于SMTP账户的密码
    password = "123456a"

    #构建SMTP对象
    smtp = smtplib.SMTP()

    #连接到SMTP服务
    con = smtp.connect(smtpserver, smtpport)
    print("连接结果：", con)

    #登录smtp服务
    log = smtp.login(username, password)
    print("登录结果：", log)

    #发送邮件
    print(receivers)
    res = smtp.sendmail(sender, receivers, msg.as_string())
    print("邮件发送结果:", res)

    #退出
    smtp.quit()
    print("send email finish")
'''
import smtplib
from email.header import Header
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

if __name__ == "__main__":
    print("发送附件示例")

    #邮件发送者
    sender = "deep_test@126.com"

    #邮件接收地址列表
    receivers = "673250728@qq.com"

    #发送内容构建
    #text表示发送内容为文本格式
    msg = MIMEMultipart()
    msg["From"] = "deep_test@126.com"
    msg["To"] = receivers

    #构建邮件标题
    msg["subject"] = Header("开源优测_DeepTest", "utf-8")

    #构建邮件正文内容
    msg.attach(MIMEText("微信公众号，开源优测", "plain", "utf-8"))
    #构造附件，多个附件同理
    attach1 = MIMEText(open("iniFile.py", "rb").read(), "base64", "utf-8")
    attach1["Content-Type"] = "application/octest-stream"

    #这里filename随便写，将会在邮件中显示
    attach1["Content-Disposition"] = "attachment;filename=code.py"

    #关联附件到邮件中
    msg.attach(attach1)

    #SMTP服务
    smtpserver = "smtp.126.com"
    smtpport = 25

    #大送人邮件密码或专用于SMTP账户用户名
    username = "deep_test"

    #发送人邮件密码或专用于SMTP账户的密码
    password = "123456a"

    #构建SMTP对象
    smtp = smtplib.SMTP()

    #连接到SMTP服务
    con = smtp.connect(smtpserver, smtpport)
    print("连接结果：", con)

    #登录smtp服务
    log = smtp.login(username, password)
    print("登录结果：", log)

    #发送邮件
    print(receivers)
    res = smtp.sendmail(sender, receivers, msg)
    print("邮件发送结果:", res)

    #退出
    smtp.quit()
    print("send email finish")

'''
#-*-coding:utf-8
__author__ = "Lakisha"

import smtplib
from email.mime.text import MIMEText
from email.header import Header

if __name__ == "__main__":
    print("发送HTML邮件示例")

    #邮件发送者
    sender = "deep_test@126.com"

    #邮件接收地址列表
    receivers = "673250728@qq.com"

    #发送内容构建
    #text表示发送内容为文本格式
    msg = MIMEText("<p>微信公众号：开源优测</p><a href='http://www.testingunion.com>开源优测社区</a>'", "html", "utf-8")
    msg["From"] = "deep_test@126.com"
    msg["To"] = receivers

    #构建邮件标题
    msg["subject"] = Header("开源优测DeepTest", "utf-8")

    #SMTP服务
    smtpserver = "smtp.126.com"
    smtpport = 25

    #大送人邮件密码或专用于SMTP账户用户名
    username = "deep_test"

    #发送人邮件密码或专用于SMTP账户的密码
    password = "123456a"

    #构建SMTP对象
    smtp = smtplib.SMTP()

    #连接到SMTP服务
    con = smtp.connect(smtpserver, smtpport)
    print("连接结果：", con)

    #登录smtp服务
    log = smtp.login(username, password)
    print("登录结果：", log)

    #发送邮件
    print(receivers)
    res = smtp.sendmail(sender, receivers, msg.as_string())
    print("邮件发送结果:", res)

    #退出
    smtp.quit()
    print("send email finish")
'''