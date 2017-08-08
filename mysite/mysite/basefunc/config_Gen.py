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
	#从db_config.yaml中读出配置数据
	data = file(filepath , "rb")
	urls = []
	for line in data.read().split('\n'):
		print "line=%s"%line
		if line.strip() != '':
			existDB = json.loads(line)
			print json.loads(existDB)['usrname']
			urls.append(json.loads(existDB)['usrname'])
	if item in urls:
		return False
	else:
		return True

		#然后判断，如果参数item存在于文件里面，就返回已经存在		
		# if item == json.loads(existDB)['url']:
		# 	print "xxxxxxx%s"%json.loads(existDB)['url']
		# 	ret['retcode'] = "已经存在"
		# 	return False
		# else:
		# 	return True


def db_conf_gen(**db):
	ret = {}
	data = json.loads(db['config'][0])
	print "url = %s"%data['url']
	path = "/".join([os.getcwd() , "mysite/config/db_conf.yaml"])
	print path
	conf = open(path , 'a+')
	# data_len = os.path.getsize(path)
	print ifexist(data['url'] , path)
	if ifexist(data['url'] , path):
		ret['retcode'] = "增加一条数据库信息"
		conf.write(json.dumps(db['config'][0]) + '\n')
		conf.close()
	else:
		ret['retcode'] = "已经存在了"
	return ret