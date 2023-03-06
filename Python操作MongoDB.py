#!/usr/bin/env python
import pymongo
# -*- coding:utf-8 -*-

from pymongo import MongoClient

conn = MongoClient('10.201.49.80', 28018)
#client = pymongo.MongoClient("mongodb://10.201.49.80:28018/")

#连接mydb数据库,账号密码认证

db = conn.energy #连接mydb数据库，没有则自动创建

db.authenticate("insread", "insread#135pwd")

my_set = db.MeterValue4New #使用test_set集合，没有则自动创建

for i in my_set.find():
    print(i)