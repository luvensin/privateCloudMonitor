#-*- coding:utf-8 -*-
import sys
sys.path.append('../../')

import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")

import django
django.setup()

from siteDemo.models import Rtable

class classification(object):
    def __init__(self):
        pass
    def classificate(slef):
        ecs = []
        rds = []
        ads = []
        odps = []
        oss = []
        galaxy = []
        docker = []
        ots = []
        slb = []
        total = Rtable.objects.all().values()
        total_len = len(total)
        for item in  total:
            if item["product"] == "ecs":
                ecs.append(item)
            if item['product'] == "rds":
                rds.append(item)
            if item['product'] == "ads":
                ads.append(item)
            if item['product'] == "odps":
                odps.append(item)
            if item['product'] == "oss":
                oss.append(item)
            if item['product'] == "galaxy":
                galaxy.append(item)
            if item['product'] == "docker":
                docker.append(item)
            if item['product'] == "ots":
                ots.append(item)
            if item['product'] == "slb":
                slb.append(item)
        return dict(total_len=total_len,ecs=ecs,rds=rds,ads=ads,odps=odps,oss=oss,galaxy=galaxy,docker=docker,ots=ots,slb=slb)
    def productPercent(self):
        ret = self.classificate()
        total =  float(ret['total_len'])
        ecs_len = (float(len(ret['ecs'])) / total)*100
        rds_len = (float(len(ret['rds'])) / total)*100
        ads_len = (float(len(ret['ads'])) / total)*100
        odps_len = (float(len(ret['odps'])) / total)*100
        oss_len = (float(len(ret['oss'])) / total)*100
        galaxy_len = (float(len(ret['galaxy'])) / total)*100
        docker_len = (float(len(ret['docker'])) / total)*100
        ots_len = (float(len(ret['ots'])) / total)*100
        slb_len = (float(len(ret['slb'])) / total)*100
        return {"ecs":round(ecs_len,2),
                "rds":round(rds_len,2),
                "ads":round(ads_len,2),
                "odps":round(odps_len,2),
                "oss":round(oss_len,2),
                "galaxy":round(galaxy_len,2),
                "dockerHost":round(docker_len,2),
                "ots":round(ots_len,2),
                "slb":round(slb_len,2)}

if __name__ == '__main__':
    pass
