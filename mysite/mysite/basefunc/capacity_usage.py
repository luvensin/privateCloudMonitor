#!/usr/bin/python
#****************************************************************#
# ScriptName: test.py
# Author: $SHTERM_REAL_USER@alibaba-inc.com
# Create Date: 2017-03-30 22:34
# Modify Author: $SHTERM_REAL_USER@alibaba-inc.com
# Modify Date: 2017-04-07 14:52
# Function: 
#***************************************************************#
import yaml
import MySQLdb
from MySQLdb import *
import re
import os
import sys
minirds_path = '../../../L1workdir/'

def load_minirds():
    ret = yaml.load(open("%sminirds-db-conf.yml"%minirds_path))
    return ret['db-installer']['DB_MYSQL_houyiregiondb']
def houyiregiondb():
    vm_info=[]
    nc_info=[]
    get_db_info=yaml.load(load_minirds())
    config = {"host":get_db_info['url'],
              "port":get_db_info['port'],
              "user":get_db_info['superuser'],
              "passwd":get_db_info['superpassword'],
              "db":get_db_info['superuser'],
              "cursorclass":MySQLdb.cursors.DictCursor}
    connection = MySQLdb.Connect(**config)
    cur = connection.cursor()
    ret = cur.execute('select vcpu,name,user_id,nc_id,memory,host_name from vm where status like "runn%"')
    for item in cur.fetchall():
        vm_info.append(item)
    ret2 = cur.execute('select nc.id,ip,used_cpu,nc_cpu,used_memory,nc_memory from nc,nc_resource where nc.id=nc_resource.id')
    for item in cur.fetchall():
        nc_info.append(item)
    cur.close()
    connection.close()
    f_vm = open('vm_info.yaml','w')
    f_nc = open('nc_info.yaml','w')
    yaml.dump(vm_info,f_vm)
    yaml.dump(nc_info,f_nc)
    f_vm.close()
    f_nc.close()
if __name__ == '__main__':
    pass
