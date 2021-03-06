# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render_to_response
#from models import rtable 
import json
import sys
sys.path.append('../')
import os
from mysite.basefunc import update_rtable , db ,ecs_module , analystic , config_Gen , minirds_conf
from mysite.config import parse_data_ecs , parse_data_ecs_pangu
# Create your views here.
from django.utils.safestring import SafeString
import yaml
#home page
# ---------------------------------------------------------------------------------
# def homeDataParse(request):
# 	ret = update_rtable.Rtable_info().update_db()
# 	rows = Rtable.objects.all()
# 	r = {"data":list(rows.values())}
# 	return HttpResponse(json.dumps(data))
def homePage(request):
	# ret = update_rtable.Rtable_info().update_db()
	# rows = Rtable.objects.all()
	# rtable = list(rows.values())
	data = minirds_conf.read_minirds_conf()
	return render(request , "home_page.html" , {"data" : data})

# --------------------------------ecs主页信息-------------------------------------
def ecsPage(request):
	ret = ecs_module.ECS_info().update_ecs()
	print ret
	return render_to_response("product_list.html")
def ecsData(request):
	ecs_nc = Ecs.objects.all().values()
	data = {"data":list(ecs_nc)}
	return HttpResponse(json.dumps(data) , content_type='application/json') 
def lock(request):

	print request.POST
	print "function lockNC"
	# do something here 在ecs ag上面执行锁定nc ，然后返回结果
	return HttpResponse("lockNc")
def unlock(request):

	print request.POST
	# do something here 在ecs ag上面执行解锁nc ，然后返回结果
	return HttpResponse("unlockNc")
def monitor(request):
	print request.POST
	return HttpResponse("monitor")
# ------------------------------------大数据主页面-----------------------------------
def dataAnalysis(request):
	return render_to_response("resourceAnalysis.html")
def mainPage(request):
    print request.method
    ret = analystic.classification().productPercent()
    print ret
    return HttpResponse(json.dumps(ret))
# ------------------------------------ecs数据页面-----------------------------------
def EcsDataShow(request):
	data = parse_data_ecs.parse_stageB()
	ncs = {}
	nc_id = []
	for nc in data['nc_cpu']:
		ncs['ecsnc_id'] = nc['nc']
		ncs['ecsnc_ip'] = nc['ip']
		nc_id.append(dict(ncs))
	return render(request ,"ecs_DataShow.html",{'data':nc_id})
def ecsDataPanel(request):
	data = parse_data_ecs.parse_stageB()
	return HttpResponse(json.dumps(data))
def ecsDataPangu(request):
	ecs_pangu_data = parse_data_ecs_pangu.parse_srv_status()
	data = {'data' : ecs_pangu_data}
	return HttpResponse(json.dumps(data))
def offline_ecs_pangu(request):
	print request.POST
	print "offline"
	# do something here 在ecs ag上面执行锁定盘古然后下线盘古 ，然后返回结果
	return HttpResponse("offline")
def shutdown_ecs_pangu(request):
	print request.POST
	#关机盘古的，没什么鸟用的功能，慎用
	print "requested function from xiaoming"
	return HttpResponse("小明要求的，没什么卵用")
# ------------------------------------OSS数据页面------------------------------------
def OssDataShow(request):
	return render_to_response("oss_DataShow.html")
# ------------------------------------配置页面---------------------------------------

def parseConf(request):
	return render_to_response("config.html")
def getConf(request):
	ret = {}
	if "db" == json.loads(request.POST['config'])['confType']:
		ret = config_Gen.db_conf_gen(**request.POST)
	else:
		print "urlconf"
	
	return HttpResponse(json.dumps(ret))
#-----------------------------------------------------------------------------------


def refresh(request):
	table = update_rtable.Rtable_info()
	table.update_db()
	data = {"ret":"ok"}
	return HttpResponse(json.dumps(data))

def table_test(request):
	return render_to_response("test.html")



def Conf(request):
	if request.method == "GET":
		getFromDB = Dbinfo.objects.all()
		print getFromDB
		return render(request,"config.html",{"getFromDB":getFromDB.values()})
		# return HttpResponse(getFromDB)
	else:
		data = request.POST
		h_ = data['host']
		P_ = data['port']
		n_ = data['dbname']
		p_ = data['password']
		result = db.DBinfo().writeDB(h_,n_,P_,p_)
		# return render(request,"config.html",{"retCode":result})
		return HttpResponse(json.dumps(result))
	# if request.method == "POST":
	# 	print request.POST
	# 	return HttpResponse("ok")
	# 	return render(request,"config.html",{"retcode":"True"})
