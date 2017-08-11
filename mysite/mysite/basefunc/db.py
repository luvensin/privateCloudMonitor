#-*- coding:utf-8 -*-
import sys
sys.path.append('../../')

import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")

import django
django.setup()

from siteDemo.models import Dbinfo
class DBinfo(object):
    def __init__(self):
        pass
    def writeDB(self,host , name , port , passwd):
    	ret={'retCode':'0','result':'null'}
    	hosts = []
    	try:
    		hosts_list = Dbinfo.objects.all().values('HOST')
    		for i in hosts_list:
    			hosts.append(i['HOST'])
    		ifExist = host in hosts
    		if ifExist:
    			Dbinfo.objects.filter(HOST=host).update(PORT=port,USER=name,PASSWD=passwd)
    			ret['result'] = "update one item"
    		else:
    			Dbinfo.objects.create(HOST=host,PORT=port,USER=name,PASSWD=passwd)
    			ret['result'] = "insert one item"
    	except Exception as e:
    		ret['result'] = "some error occourd when insert item into DB %s"%e
    		ret['retCode'] = '10'
    	return ret

if __name__ == '__main__':
	pass


