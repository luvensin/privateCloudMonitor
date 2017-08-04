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
                row['sn'] = line.get('ServiceTag').strip()
                row['product'] = line.get('product').strip()
                row['ip'] = line.get('IP').strip()
                row['hostname'] = line.get('hostname').strip()
                row['os'] = line.get('OS').strip()
                row['clone_scripts'] = line.get('装机模版').strip()
                row['machine'] = line.get('机型').strip()
                row['status'] = self.icmp(line.get('ip'))
                rows.append(dict(row))
        return rows
            
    
    def rules(self,sn,product,ip,hostname,os,clone_scripts,machine,status):
      ret = {"retCode":0,"description":"null"}
      sn_list = []
      try:
        all_sn = Rtable.objects.all().values('sn')
        for i in all_sn:
          sn_list.append(i['sn'])
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
    pass

