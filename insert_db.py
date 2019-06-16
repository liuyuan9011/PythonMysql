# -*- coding: utf-8 -*-

import MySQLdb
import random
from const import *

MerchantMap = dict()
BizMap = dict()


def get_merchant_id():
    while True:
        id = random.randint(1, 99999999)
        if id in MerchantMap:
            continue
        MerchantMap[id] = 1
        return 'merchant_%s' % id


def get_biz_id():
    while True:
        id = random.randint(1, 99999999)
        if id in BizMap:
            continue
        BizMap[id] = 1
        return 'biz_%s' % id


# 将merchant_id写入文件
def insert_sql(db_handler, cursor_handler):
    file_handler = open(MERCHANT_FILE, mode='w')
    for i in range(0, DEFAULT_INSERT_NUM):
        biz_id = get_biz_id()
        merchant_id = get_merchant_id()
        sql1 = SQL_FORMAT_1 % (biz_id, merchant_id)
        sql2 = SQL_FORMAT_2 % biz_id
        # cursor_handler.execute(sql1)
        # cursor_handler.execute(sql2)
        file_handler.write(merchant_id + '\n')
    file_handler.close()


# 读取文件
def read_file(file_name):
    file_handler = open(file_name)
    for line in file_handler:
        print "===========", line[:-1]
    file_handler.close()


# 请先安装
# 参考链接: https://www.runoob.com/python/python-mysql.html
# pip install pymysql
if __name__ == '__main__':
    # 打开数据库连接
    db = MySQLdb.connect(host=DbConfig.host, user=DbConfig.user, port=DbConfig.port, passwd=DbConfig.password,
                         charset='utf8')
    # 使用cursor()方法获取操作游标
    cursor = db.cursor()

    # example: 使用execute方法执行SQL语句
    cursor.execute(TEST_SQL)
    # 使用 fetchall() 方法获取所有数据
    data = cursor.fetchall()
    for row in data:
        print row

    insert_sql(db, cursor)
    read_file(MERCHANT_FILE)

    # 测试随机生成merchant_id
    # for i in range(10):
    #     print '=================', get_merchant_id()

    # 关闭数据库连接, 关闭文件
    db.close()
