# -*- coding: utf-8 -*-

import sys
import MySQLdb
from db import get_session
from const import *

# 请先安装
# 参考链接: https://www.runoob.com/python/python-mysql.html
# pip install pymysql
if __name__ == '__main__':
    # 打开数据库连接
    db = MySQLdb.connect(DB_CONF['host'], DB_CONF['user'],  "testuser", "test123", "TESTDB", charset='utf8')

    # 使用cursor()方法获取操作游标
    cursor = db.cursor()

    # 使用execute方法执行SQL语句
    cursor.execute("SELECT VERSION()")

    # 使用 fetchone() 方法获取一条数据
    data = cursor.fetchone()

    print("Database version : %s " % data)

    # 关闭数据库连接
    db.close()
