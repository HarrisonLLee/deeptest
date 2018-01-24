#!/usr/bin/env python
# encoding: utf-8
import smtplib
from email.mime.text import MIMEText
from email.header import Header

if __name__ == '__main__':
	print ('发送文本邮件示例')

	'''邮件的发送者'''
	Sender = '15021847009@163.com'

	'''邮件接收地址列表'''
	Receivers = '1178821890@qq.com'

	'''发送内容构建'''
	'''text标识发送内容为文本格式'''
	msg = MIMEText('微信公众号：开源优测',_subtype='plain',_charset='utf-8')
	msg['From'] = Sender
	msg['To'] = Receivers

	'''构建邮件的标题'''
	msg['Subject'] = Header('开源优测_DeepTest','utf-8')

	'''smtp服务'''
	smtpserver = 'smtp.163.com'

	'''发送人邮件用户名或专用于smtp账户用户名'''
	username = Sender

	'''发送人邮件密码或专用于smtp账户的密码'''
	password = 'xxxx'

	'''构建smtp对象'''
	smtp = smtplib.SMTP()

	'''连接到smtp服务'''
	smtp.connect(smtpserver)


	'''登录smtp服务'''
	smtp.login(username, password)


	'''发送邮件'''
	smtp.sendmail(Sender,Receivers,msg.as_string())

	'''退出'''
	smtp.quit()
	print ('send email finish')

