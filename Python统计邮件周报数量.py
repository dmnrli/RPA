#! /usr/bin/env python3.4
#coding : utf-8
import getpass
import imaplib
from imapclient import IMAPClient

import imaplib,string,os,email
from email.parser import Parser
from email.header import decode_header

#服务器网址
hostname = 'outlook.office365.com'
#服务器端口
host = 995
#用户名
username = 'rivern.li@multek.com'
#密码
passwd = 'Www@999'
#passwd = getpass.getpass()

#链接服务器
mail = imaplib.IMAP4("https://outlook.office.com/mail/")


#mail = imaplib.IMAP4_SSL(hostname,host)
with imaplib.IMAP4(host= hostname,port=995) as M:
#with imaplib.IMAP4_SSL(hostname) as M:
    M.login(user=username,password=passwd)
    M.select("INBOX")
    M.list()
    M.close()
    M.logout()
'''
'''
try:
    #登录账号
    print("Ready!")
    mail.login(username,passwd)
    print("查询")
except Exception as err:
    print(err)

