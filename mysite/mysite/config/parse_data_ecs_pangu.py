import commands

import sys
sys.path.append('../../')


import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")

import django
django.setup()



path = os.getcwd()

pangu_info = "/".join([path,"mysite/config/ecs_pangu.txt"])

def parse_srv_status():
    oss_srv_stat = {}
    ret = []
    pangu_srv_status = commands.getoutput("cat %s |grep -Ei \"normal|disconnected\""%pangu_info)
    split_data = pangu_srv_status.split('\n')
    for srv in split_data:
        oss_srv_stat["status"] = srv.split()[1]
        oss_srv_stat['ip'] = srv.split()[5].split('//')[1]
        oss_srv_stat['hostname'] = srv.split()[6]
        ret.append(dict(oss_srv_stat))
    return ret


