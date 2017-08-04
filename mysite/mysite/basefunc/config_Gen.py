# -*- coding: utf-8 -*-
import sys
sys.path.append('../../')

import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")

import django
django.setup()
import yaml
import json
def ifexist(item , filepath):
	ret = {}
	data = file(filepath , "rb")
	for line in data.read().split('\n'):
		existDB = json.loads(line)
		
		if item == json.loads(existDB)['url']:
			ret['retcode'] = "已经存在"
			return False
			break
		else:
			return True


def db_conf_gen(**db):
	ret = {}
	data = json.loads(db['config'][0])
	path = "/".join([os.getcwd() , "mysite/config/db_conf.yaml"])
	conf = open(path , 'a+')
	print data['url']
	if not os.path.getsize(path) or ifexist(data['url'] , path):
		ret['retcode'] = "增加一条数据库信息"
		conf.write(json.dumps(db['config'][0]) + '\n')
		conf.close()
	else:
		ret['retcode'] = "已经存在了"
	print ret
	return ret
