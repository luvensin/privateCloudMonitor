#-*- coding:utf-8 -*-
import sys
sys.path.append('../../')

import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")

import django
django.setup()

import logging

#from django.core.management import setup_environ

import csv
from siteDemo.models import Rtable

class Rtable_info(object):

    global filePath
    filePath = os.path.join(os.path.dirname(__file__),'rtable.csv')
    def __init__(self):
        pass 
    def icmp(self,ip):
      import commands
      cmd = 'ping %s -c 1 '%ip
      status = commands.getstatus(cmd)
      if status == 0 :
        return "alive"
      else:
        return "dead"

    def info(self):
        ret = {'code':0,"desc":"ok"}
        rows = []
        row={}

        data = csv.DictReader(file(filePath,'rb'))
        for line in data:
            if line.get('机型') != 'docker':
                row['serviceTag'] = line.get('ServiceTag').strip()
                row['product'] = line.get('product').strip()
                row['new_appgroup'] = line.get('new_appgroup').strip()
                row['node'] = line.get('node').strip()
                row['product_line'] = line.get('产品线').strip()
                row['hostname'] = line.get('hostname').strip()
                row['ip'] = line.get('IP').strip()
                row['os'] = line.get('OS').strip()
                row['clone_scripts'] = line.get('装机模版').strip()
                row['machine_type'] = line.get('机型').strip()
                row['idc'] = line.get('机房').strip()
                row['room'] = line.get('包间').strip()
                row['rack_number'] = line.get('机柜编号').strip()
                row['server_position'] = line.get('机位').strip()
                row['rack_position'] = line.get('机柜位置').strip()
                row['asw_number'] = line.get('ASW编号').strip()
                row['all_product'] = line.get('所有产品').strip()
                row['node_quantity'] = line.get('节点数量').strip()
                row['node_config'] = line.get('节点配置').strip()
                row['area'] = line.get('区域').strip()
                row['service'] = line.get('service').strip()
                row['serviceInstanceNo'] = line.get('serviceInstanceNo').strip()
                row['runtimeResourceLimit'] = line.get('runtimeResourceLimit').strip()
                row['region'] = line.get('region').strip()
                rows.append(dict(row))
        return rows
            
    
    def rules(self,*row):
      ret = {"retCode":0,"description":"null"}
      sn_list = []
      try:
        all_sn = Rtable.objects.all().values('serviceTag')
        for i in all_sn:
          sn_list.append(i['serviceTag'])
        ifexist = sn in sn_list
        if ifexist:
          Rtable.objects.filter(sn=sn).update(product=product,ip=ip,hostname=hostname,os=os,clone=clone_scripts,machine=machine,status=status)
          ret['description'] = 'update one item'
        else:
          Rtable.objects.create(sn=sn,product=product,ip=ip,hostname=hostname,os=os,clone=clone_scripts,machine=machine,status=status)
          ret['description'] = 'insert one item'
      except Exception as e:
        print e
        ret['retCode'] = 1
        ret['description'] = 'some error occourd during update db info'
      return ret
    def update_db(self):
      result = []
      for line in self.info():
        sn = line['sn']
        product = line['product']
        ip = line['ip']
        hostname = line['hostname']
        os = line['os']
        clone_scripts = line['clone_scripts']
        machine = line['machine']
        status = line['status']
        result.append(self.rules(sn,product,ip,hostname,os,clone_scripts,machine,status))
      return result
if __name__ == '__main__':
    print Rtable_info().info()
