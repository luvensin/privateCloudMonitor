# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Publisher(models.Model):
	name = models.CharField(max_length=30)
	address = models.CharField(max_length=50)
	city = models.CharField(max_length=60)
	country = models.CharField(max_length=50)
	website = models.URLField()

class Author(models.Model):
	name = models.CharField(max_length=100)
	email = models.CharField(max_length=100)

	def __unicode__(self):
		return '%s %s' % (self.name, self.email)

class Lu(models.Model):
	name = models.CharField(max_length=40)
	age = models.CharField(max_length=5)
	address = models.CharField(max_length=100)
	email = models.CharField(max_length=30)
	weichat = models.CharField(max_length=30) 	
	phone = models.CharField(max_length=30)

	def __unicode__(self):
		return "name : %s , age : %s , address : %s , email : %s , weichat : %s , phone : %s"%(self.name , self.age , self.address , self.email , self.weichat , self.phone)

# Create your models here.

class Rtable(models.Model):
	sn = models.CharField(max_length=20)
	product = models.CharField(max_length=30)
	ip = models.CharField(max_length=30)
	hostname = models.CharField(max_length=40)
	machine = models.CharField(max_length=10)
	os = models.CharField(max_length=30)
	clone = models.CharField(max_length=30)
	cpu_type = models.CharField(max_length=40)
	cpu_phy = models.CharField(max_length=30)
	cpu_cores = models.CharField(max_length=5)
	mem = models.CharField(max_length=15)
	disk = models.CharField(max_length=15)
	status = models.CharField(max_length=5)

	def __unicode__(self):
		return ("sn:%s , product:%s , ip:%s , hostname:%s , machine:%s , os:%s , clone:%s , cpu_type:%s , cpu_phy:%s , cpu_cores:%s , mem:%s , disk:%s , status:%s "
				%(self.sn,self.product,self.ip,self.hostname,self.machine,self.os,self.clone,self.cpu_type,self.cpu_phy,self.cpu_cores,self.mem,self.disk,self.status))
class Ecs(models.Model):
	sn = models.CharField(max_length=20)
	hostname = models.CharField(max_length=30)
	ip = models.CharField(max_length=30)
	nc_id = models.CharField(max_length=10)
	status = models.CharField(max_length=10)
	def __unicode__(self):
		return ("sn:%s , hostname%s , ip:%s , nc_id:%s , status:%s"
				%(self.sn , self.hostname , self.ip , self.nc_id , self.status))
class Dbinfo(models.Model):
	HOST = models.CharField(max_length=30)
	PORT = models.CharField(max_length=5)
	USER = models.CharField(max_length=20)
	PASSWD = models.CharField(max_length=30)
	def __unicode__(self):
		return ("host:%s , port:%s , user:%s , passwd:%s" %(self.HOST , self.PORT , self.USER , self.PASSWD))











