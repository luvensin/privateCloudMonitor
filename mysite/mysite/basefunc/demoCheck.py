#!/home/tops/bin/python
#-*- coding:utf-8 -*-
#****************************************************************#
# ScriptName: demoCheck.py
# Author: 随便写写
# Create Date: 2017-06-19 19:21
# Modify Date: 2017-06-21 09:21
# Function: dlya plaverka plavilinasti na platfolma
#***************************************************************#
import sys
sys.path.append("../../")
from optparse import OptionParser
import main.tools.rtable as rtable
import yaml
import json
import commands

reload(sys)
sys.setdefaultencoding('utf-8')

R_DATA = rtable.load_csv_file()
global PHY_HOST
global STANDARD
STANDARD = json.load(file('Standar.json','rb'))
PHY_HOST = []
for host in R_DATA['content']['rtableinfo']:
    if host['deploymentType'] in ['Native','Hardware']:
        PHY_HOST.append(host)
ECS = []
ADS = []
SLB = []
DOCKER = []
RDS = []
YUNDUN = []
OTS = []
GALAXY = []
SLS_OTS = []
ODPS = []
OSS = []

for Line in PHY_HOST:
  if Line['product'] == 'ecs':
    ECS.append(Line)
  if Line['product'] == 'ads':
    ADS.append(Line)
  if Line['product'] == 'slb':
    SLB.append(Line)
  if Line['product'] == 'docker':
    DOCKER.append(Line)
  if Line['product'] == 'rds':
    RDS.append(Line)
  if Line['product'] == 'yundun':
    YUNDUN.append(Line)
  if Line['product'] == 'ots' and Line['service'] == 'public':
    OTS.append(Line)
  if Line['product'] == 'galaxy':
    GALAXY.append(Line)
  if Line['product'] == 'sls':
    SLS_OTS.append(Line)
  if Line['product'] == 'odps':
    ODPS.append(Line)
  if Line['product'] == 'oss':
    OSS.append(Line)



usage = '''工具按照R表产品进行检查，
           首先要确保当前目录下存在“Standar.json”文件，文件中是各产品的磁盘挂载和大小标准。
           目前囊括的产品有 ecs,rds,ads,slb,docker宿主机,yundun,ots,galaxy,sls,odps,oss，
           脚本的使用方法比较简单，可以按照产品分类对某一产品进行查验，也可以对多个产品进行查验。进行单个产品查验
           的时候只需要工具脚本后跟相对应产品的名称，类似于“--ecs” “--slb”等，如果对多个产品进行查验只需要后面跟
           多个参数即可。
           对于那些查验主机正确性检查错误的，会在当前目录下产生对应的日志文件，例如：ecs检查，如果有错会在当前目录
           下产生ECS.log ，其他产品也是相同。

        '''
parser = OptionParser(usage=usage)

parser.add_option("-E" , "--ecs" , action="store_true" ,dest="ecs"  ,help="检查ecs主机装机正确性")
parser.add_option("-A" , "--ads" , action="store_true" ,dest="ads"  ,help="检查ads主机装机正确性")
parser.add_option("-S" , "--slb" , action="store_true" ,dest="slb"  ,help="检查slb主机装机正确性")
parser.add_option("-D" , "--docker" , action="store_true" ,dest="docker"  ,help="检查docker宿主机装机正确性")
parser.add_option("-R" , "--rds" , action="store_true" ,dest="rds"  ,help="检查rds linux主机装机正确性")
parser.add_option("-Y" , "--yundun" , action="store_true" ,dest="yundun"  ,help="检查yundun主机装机正确性")
parser.add_option("-O" , "--odps" , action="store_true" ,dest="odps"  ,help="检查odps主机装机正确性")
parser.add_option("-G" , "--galaxy" , action="store_true" ,dest="galaxy"  ,help="检查galaxy主机装机正确性")
parser.add_option("-L" , "--sls" , action="store_true" ,dest="sls"  ,help="检查多级混布sls主机装机正确性")
parser.add_option("-T" , "--ots" , action="store_true" ,dest="ots"  ,help="检查ots主机装机正确性")
parser.add_option("-s" , "--oss" , action="store_true" , dest="oss" ,help="检查oss主机装机正确性")

(options , args) = parser.parse_args()

def sn(ip):
    ret = {"code":0,"description":"SUCCESS","sn":"null"}
    status,output = commands.getstatusoutput('ssh %s "dmidecode -t 1|grep Seri"'%ip)
    if status == 0:
        ret['sn'] = output.split(":")[1].strip()
    else:
        ret['code'] = 1
        ret['description'] = "FAILED"
    return ret
def hostname(ip):
    ret = {"code":0,"description":"SUCCESS","hostname":"null"}
    status,output = commands.getstatusoutput('ssh %s "hostname"'%ip)
    if status == 0:
        ret['hostname'] = output.strip()
    else:
        ret['code'] = 1
        ret['description'] = "FAILED"
    return ret
def os_clone(ip):
    ret = {"code":0,"description":"SUCCESS","os":"null","clonescript":"null"}
    status,output = commands.getstatusoutput('ssh %s "cat /var/clone/clone_info"'%ip)
    if status == 0:
        clone_data = json.loads(output)
        ret['os'] = clone_data['os'].strip()
        ret['clonescript'] = clone_data['clonescript'].strip()
    else:
        ret['code'] = 1
        ret['description'] = "FAILED"
    return ret
def memory(ip):
    ret = {'code':0,'description':'SUCCESS','memory':'null'}
    status,output = commands.getstatusoutput('ssh %s "hwconfig|grep Memory"'%ip)
    if status == 0:
        ret['memory'] = output.split()[3].strip()
    else:
        ret['code'] = 1
        ret['description'] = "FAILED"
    return ret
def disk_vol(ip):
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
    
def disk_partition(ip):
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

def log_writer(filename,dt):
  f = open(filename,'a')
  data = json.dumps(dt,sort_keys=True,indent=2)
  f.write(data)
  f.close()

def start(Type,product):
  if len(product) == 0:
    print "产品%s不存在"%Type
    sys.exit(1)
  Type = Type.upper()
  ret = {}
  count = 0
  for line in product:
    partition = STANDARD[Type][line['machine_type']]['partition']
    disk_vol = STANDARD[Type][line['machine_type']]['disk_vol']
    ret = check(line['ip'],line['sn'],line['hostname'],partition,disk_vol,line['os'],line['clone_script'])
    count = count + 1
    percent = float(count) / float(len(product))
    percent = str(int(percent * 100))
    sys.stdout.write("\033[1;32;40m正在检查 [ %s ] 主机 : 进度 = \033[0m"%Type + percent +" %  "+"\r")
    sys.stdout.flush()
    if 'false' in ret.values():
      print "在%s检测到错误,详细请看%s.log"%(line['ip'],Type)
      log_writer('%s.log'%Type,dict(FALED=ret))
      
 #通过ssh IP检查sn，hostname，磁盘挂载，磁盘大小，操作系统，装机模版，内存             
def check(ip,serviceTag,Hostname,Partition,Disk_Vol,os,clone_script):
  ret = {}
  ret['ip'] = ip
  if sn(ip)['sn'] == serviceTag:
    ret['sn'] = "true"
  else:
    ret['sn'] = "fata %s"%sn(ip)['sn']
  if hostname(ip)['hostname'] == Hostname:
    ret['hostname'] = "true"
  else:
    ret['isSuccess'] = "false"
    ret['hostname'] = {"wrong":hostname(ip)['hostname'],"right":Hostname}
  if os_clone(ip)['os'] == os:
    ret['os'] = 'true'
  else:
    ret['isSuccess'] = "false"
    ret['os'] = {"wrong":os_clone(ip)['os'],"right":os}
  if os_clone(ip)['clonescript'] == clone_script:
    ret['clone_script'] = 'true'
  else:
    ret['isSuccess'] = "false"
    ret['clone_script'] = 'fata %s'%os_clone(ip)['clonescript']
  if disk_partition(ip)['partition'] == Partition:
    ret['partition'] = 'true'
  else:
    ret['isSuccess'] = "false"
    ret['partition'] = 'fata %s'%disk_partition(ip)['partition']
  if disk_vol(ip)['disk_vol'] == Disk_Vol:
    ret['disk_vol'] = "true"
  else:
    ret['isSuccess'] = "false"
    ret['disk_vol'] = {"wrong":disk_vol(ip)['disk_vol'],"right":Disk_Vol}
  return ret

    
    
if __name__ == "__main__":
    #print disk_partition(sys.argv[1])
    if len(sys.argv[1::]) < 1:
      print "use '-h' or '--help'  for more details"
    if options.ecs:
      start('ecs',ECS)
    if options.ads:
      start('ads',ADS)
    if options.slb:
      start('slb',SLB)
    if options.docker:
      start('docker',DOCKER)
    if options.rds:
      start('rds',RDS)
    if options.yundun:
      start('yundun',YUNDUN)
    if options.ots:
      start('ots',OTS)
    if options.sls:
      start('sls',SLS_OTS)
    if options.odps:
      start('odps',ODPS)
    if options.galaxy:
      start('galaxy',GALAXY)
    if options.oss:
      start('oss',OSS)

