#!/usr/bin/env Python
# coding=utf-8

import MySQLdb

conn=MySQLdb.connect(host='127.0.0.1',port=3306,user='root',passwd='zhoulin',db='awesome',charset='utf-8')#连接对象

cur=conn.cursor() #游标对象