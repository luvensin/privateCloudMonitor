#-*- coding:utf-8 -*-
import sys
sys.path.append('../../')

import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")

import django
django.setup()


from update_rtable import Rtable_info
from siteDemo.models import Ecs , Rtable

class check_item(object):
    def __init__(self):
		pass
    def disk_vol(self,ip):
        ret = {"code":0,"description":"SUCCESS","disk_vol":"null"}
        status,output = commands.getstatusoutput('ssh %s "hwconfig|grep Disk:"'%ip)
        if status == 0:
            vol = []
            for line in output.split("\n"):
                vol.append(line.split()[1]+" "+line.split()[3])
                ret["disk_vol"] = vol
            else:
                ret['code'] = 1
                ret['description'] = 'FAILED'
        return ret
    def disk_partition(self,ip):
        ret = {"code":0,"description":"SUCCESS","partiton":"null"}
        status,output = commands.getstatusoutput('ssh %s "df -lh|grep -v File"'%ip)
        if status == 0:
            partition = []
            for line in output.split("\n"):
                partition.append(line.split()[0]+" "+line.split()[5])
                ret['partition'] = partition
        else:
            ret["code"] = 1
            ret["description"] = "FAILED"
        return ret
    def checkResult(self,ip,type):
        ret = {}
        if self.disk_partition(ip)['partition'] == Partition:
            ret['checkItem'] = "partition"
            ret['partition'] = "true"
        else:
            ret['isSuccess'] = "false"
            ret['reason'] = 'fata %s'%self.disk_partition(ip)['partition']
        return ret



class ECS_info(object):
    def __init__(self):
        pass
    def rules(self,sn,hostname,ip,nc_id,status):
        ret = {"retCode":0,"description":"null"}
        sn_list = []
        try:
            all_sn = Ecs.objects.all().values('sn')
            for i in all_sn:
                sn_list.append(i['sn'])
            ifexist = sn in sn_list
            if ifexist:
                Ecs.objects.filter(sn=sn).update(hostname=hostname,ip=ip,nc_id=nc_id,status=status)
                ret['description'] = 'update one item'
            else:
                Ecs.objects.create(sn=sn,hostname=hostname,ip=ip,nc_id=nc_id,status=status)
                ret['description'] = 'insert one item'
        except Exception as e:
            print e
            ret['description '] = 'some error occourd during update db'
            ret['retCode'] = 1
        return ret
    def update_ecs(self):
        result = []
        for line in Rtable_info().info():
            if line['product'] == 'ecs':
                sn = line['sn']
                ip = line['ip']
                hostname = line['hostname']
                nc_id = "null"
                status = "default"

                result.append(self.rules(sn,hostname,ip,nc_id,status))
        return result


	

