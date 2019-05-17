# encoding: utf-8
#!usr/bin/python
from email.mime.text import MIMEText
from email.header import Header
import smtplib

__author__ = 'admin'

import os

def new_report(test_report):
    lists = os.listdir(test_report)
    lists.sort(key=lambda fn:os.path.getmtime(test_report + "\\" + fn))
    file_new = os.path.join(test_report,lists[-1])
    print(file_new)
    return file_new

def send_mail(file_new):
    f = open(file_new,'rb')
    mail_body = f.read()
    f.close()

    sender = 'nalabst@163.com'
    receivers = ['nalabst@126.com','137363092@qq.com']
    msg = MIMEText(mail_body,'html','utf-8')
    msg["From"] = sender
    msg["To"] = Header("接收者测试", 'utf-8')
    msg['Subject'] = Header('接口自动化测试报告','utf-8')

    smtp = smtplib.SMTP()
    smtp.connect('smtp.163.com')
    smtp.login('nalabst@163.com','bst19881117')
    smtp.sendmail(sender, receivers, msg.as_string())
    smtp.quit()
    print('邮件已发出！注意查收。')


if __name__ == '__main__':
    send_mail(new_report("F:\\pythonAutoTest\\InterfaceTestDemo\\testresult"))
