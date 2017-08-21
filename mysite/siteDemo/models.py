# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Rtable(models.Model):
	serviceTag= models.CharField(max_length=20)
	product = models.CharField(max_length=30)
	new_app_group = models.CharField(max_length=40)
	node = models.CharField(max_length=40)
	product_line = models.CharField(max_length=10)
	hostname = models.CharField(max_length=40)
	ip = models.CharField(max_length=40)
	os = models.CharField(max_length=40)
	clone_scripts = models.CharField(max_length=30)
	machine_type = models.CharField(max_length=10)
	idc = models.CharField(max_length=10)
	idc_room = models.CharField(max_length=10)
	rack_number = models.CharField(max_length=10)
	server_position = models.CharField(max_length=10)
	asw_number = models.CharField(max_length=20)
	all_product = models.CharField(max_length=10)
	node_quantity = models.CharField(max_length=5)
	node_config = models.CharField(max_length=250)
	area = models.CharField(max_length=10)
	service = models.CharField(max_length=25)
	serviceInstanceNo = models.CharField(max_length=5)
	runtimeResourceLimit = models.CharField(max_length=250)
	region = models.CharField(max_length=30)

	def __unicode__(self):
		return dict(serviceTag = self.serviceTag,
					product = self.product,
					new_app_group = self.new_app_group,
					node = self.node,
					product_line = self.product_line,
					hostname = self.hostname,
					ip = self.ip,
					os = self.os,
					clone_scripts = self.clone_scripts,
					machine_type = self.machine_type,
					idc = self.idc,
					idc_room = self.idc_room,
					rack_number = self.rack_number,
					server_position = self.server_position,
					asw_number = self.asw_number,
					all_product = self.all_product,
					node_quantity = self.node_quantity,
					node_config = self.node_config,
					area = self.area,
					service = self.service,
					serviceInstanceNo = self.serviceInstanceNo,
					runtimeResourceLimit = self.runtimeResourceLimit,
					region = self.region)







