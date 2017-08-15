#!/home/tops/bin/python
#-*- coding:utf-8 -*-
import MySQLdb
import yaml
from MySQLdb import *
'''
scripts create at 2017/08/15
use method
*create class
xx=operator("dbname")
xx.action('sql')
return datalist from your sql
'''

class operator(object):
    def __init__(self,filename,db_name):
        self.db_name = db_name
        self.filename = filename
    def connect(self):
        db_url = yaml.load(file(self.filename,'rb'))['db-installer']
        for key,val in db_url.items():
            if "_".join(["DB","MYSQL",self.db_name]) == key:
                value = yaml.load(val)
                print value
                url = value['url']
                user = value['superuser']
                password = value['superpassword']
                port = value['port']
                db = value['url'].split(".")[0]
        conn=MySQLdb.connect(host=url,user=user,passwd=password,port=port,db=db,cursorclass=MySQLdb.cursors.DictCursor)
        return conn.cursor()
    def action(self , sql):
        result = []
        db = self.connect()
        db.execute(sql)
        for data in  db.fetchall():
            result.append(data)
        db.close()
        return result
    def drop_all_tables(self , db , cmd):
        '''
        后期功能，最好不要写
        '''
        pass
    def bak_all_tables(self , db , cmd):
        '''
        2017/08/16
        '''
        pass
