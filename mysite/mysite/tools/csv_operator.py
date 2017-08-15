#-*- coding:utf-8 -*-

import csv
import os

'''
# print os.getcwd()
# path = "/alidata/L1tools/main/config/"
# f = "/Users/luvensin/Desktop/github/privateCloudMonitor/mysite/mysite/basefunc/rtable.csv"
'''
class csvReader:
    def __init__(self, filename):
        self.filename = filename

    def data(self,*keys):
    	row = {}
    	rows = []
    	data = csv.DictReader(file(self.filename,'rb'))
        for line in data:
            for key in keys:
                row[key] = line.get(key).strip()
                rows.append(dict(row))
        return rows

'''
usage : import csv_operator.csvReader as xxx
xxx(csv file name ).data('字段1','字段2','字段3',.....) 
'''


