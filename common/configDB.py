# encoding: utf-8
#!usr/bin/python
__author__ = 'admin'

from common.Log import MyLog
import pymysql
from common.readConfig import Configuration

class configDB:

    def __init__(self):
        self.log = MyLog.get_log()
        self.db = None
        self.cursor = None
        self.config = {
            'host': str(Configuration().getValue('DATABASE','host')),
            'user':Configuration().getValue('DATABASE','username'),
            'passwd':Configuration().getValue('DATABASE','password'),
            'port':int(Configuration().getValue('DATABASE','port')),
            'db':Configuration().getValue('DATABASE','database'),
            'charset':'utf8'
        }

    def connectDB(self):
        try:
            print(self.config)
            self.db = pymysql.connect(**self.config)
            self.cursor = self.db.cursor()
            self.log.logger.info("connect database success...")
            print("connect database success")
        except:
            self.log.logger.error("connect error...")
            print("connect error")

    def closeDB(self):
        self.db.close()
        self.log.logger.info("close database success...")

    def updateDelete(self, sql):
        try:
            self.cursor.execute(sql)
            self.db.commit()
            self.log.logger.info("execute %s success..." % sql)
        except:
            self.db.rollback()

    def queryData(self, sql):
        try:
            self.cursor.execute(sql)
            results = self.cursor.fetchall()
            for row in results:
                id = row[0]
                name = row[1]
                print("id=%d,name=%s" % (id,name))
            self.log.logger.info("query data success...")
        except:
            print("query error...")
            self.log.logger.error("query data error...")





if __name__ == '__main__':
    configDB().connectDB()