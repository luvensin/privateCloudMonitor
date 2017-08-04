#-*- coding:utf-8 -*-
import sys
sys.path.append('../../')

import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")

import django
django.setup()

import yaml
import json
def loadYaml():
    path = os.getcwd()
    file_vm = "/".join([path,"mysite/config/vm_info.yaml"])
    file_nc = "/".join([path,"mysite/config/nc_info.yaml"])
    data_vm = yaml.load(file(file_vm,'r'))
    data_nc = yaml.load(file(file_nc,'r'))
    return {"vm":data_vm,"nc":data_nc}

def parse_stageA():
    total = loadYaml()
    data_nc = total['nc']
    data_vm = total['vm']
    parseMem = {}
    parseCpu = {}
    result_mem = []
    result_cpu=[]
    for nc in data_nc:
        mem = []
        cpu = []
        for i in data_vm:
            if nc['id'] == i['nc_id']:
                parseMem['value'] = i['memory']
                parseMem['name'] = i['name']
                parseCpu['value'] = i['vcpu']
                parseCpu['name'] = i['name']
                mem.append(dict(parseMem))
                cpu.append(dict(parseCpu))
        mem.append(dict(value=nc['nc_memory'],name='total memory %s'%nc['id']))
        mem.append(dict(value=nc['used_memory'],name="used memory %s"%nc['id']))
        cpu.append(dict(value=nc['nc_cpu'],name='total cpu %s'%nc['id']))
        cpu.append(dict(value=nc['used_cpu'],name="used cpu %s"%nc['id']))
        result_mem.append(dict(nc=nc['id'], ip=nc['ip'], vmem=mem))
        result_cpu.append(dict(nc=nc['id'], ip=nc['ip'], vcpu=cpu))
    
    for m in result_mem:
        sum_lst = []
        nc_mem_total = 0
        nc_mem_used = 0
        for mm in m['vmem']:
            if m['nc'] not in mm['name']:
                sum_lst.append(int(mm['value']))
            else:
                if "total" in mm['name']:
                    nc_mem_total = mm['value']
                if "used" in mm['name']:
                    nc_mem_used = mm['value']
        m['vmem'].append(dict(name="free memory" , value = nc_mem_total-nc_mem_used))
        sum_mem = sum(sum_lst)
        m['vmem'].append(dict(name="other" , value = nc_mem_used - sum_mem))
    
    for c in result_cpu:
        cpu_sum_lst = []
        nc_cpu_total = 0
        nc_cpu_used = 0
        for cc in c['vcpu']:
            if c['nc'] not in cc['name']:
               cpu_sum_lst.append(cc['value'])
            else:
                if "total" in cc['name']:
                    nc_cpu_total = cc['value']
                if "used" in cc['name']:
                    nc_cpu_used = cc['value']
        c['vcpu'].append(dict(name = 'free cpu' , value = nc_cpu_total - nc_cpu_used))
        sum_cpu = sum(cpu_sum_lst)
        c['vcpu'].append(dict(name = "other" , value = nc_cpu_used - sum_cpu))
    
    return {'memory': result_mem , 'cpu' : result_cpu}
       


def parse_stageB():
    parse_memory = parse_stageA()['memory']
    parse_cpu = parse_stageA()['cpu']
    for memory in parse_memory:
        sub_mem_lst = []
        for sub_memory in memory['vmem']:
            rules = ['total memory','used memory']
            if not all(rule not in sub_memory['name'] for rule in rules):
                sub_mem_lst.append(sub_memory)
        for delete in sub_mem_lst:
            memory['vmem'].remove(delete)
    #print parse_memory
    for cpu in parse_cpu:
        sub_cpu_lst = []
        for sub_cpu in cpu['vcpu']:
            rules = ['total cpu' , 'used cpu']
            if not all(rule not in sub_cpu['name'] for rule in rules):
                sub_cpu_lst.append(sub_cpu)
        for delete in sub_cpu_lst:
            cpu['vcpu'].remove(delete)
    #print parse_cpu

    return {'nc_memory' : parse_memory , 'nc_cpu' : parse_cpu}


