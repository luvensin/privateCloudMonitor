#-*- coding:utf-8 -*-
import sys
sys.path.append('../../')

import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")

import django
django.setup()

import yaml
#read from minirds-db-config.yml push all mysql dbinfo to frontend
def read_minirds_conf():
	BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
	path = "/".join([BASE_DIR,"config/minirds-db-conf.yml"])
	data = yaml.load(file(path , 'rb'))
	db_dict = {}
	db_list = []
	for k,v in data['db-installer'].items():
		Val = yaml.load(v)
		if type(Val) is dict:
			mysql = "mysql"
			h_ = "-h%s"%Val['url']
			u_ = "-u%s"%Val['superuser']
			p_ = "-p%s"%Val['superpassword']
			P_ = "-P%s"%Val['port']
			db_list.append({"name":k , "jdbc":" ".join([mysql,h_,u_,p_,P_])})
	return db_list
	
	
