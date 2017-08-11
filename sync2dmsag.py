#!/bin/python

import subprocess
import shlex
import os
import paramiko
import commands
path = "/".join([os.getcwd() , "mysite"])
tar_pkg = "/".join([os.getcwd() , "mysite.zip"])
host = "**********"
port = "**********"
user = "root"
password = "****************"

def init():
    if os.path.isfile(tar_pkg):
        print "file exist deleting ...... "
        status,output = commands.getstatusoutput("rm -rf %s"%tar_pkg)
        if status == 0:
            print "delete pkg complated"
            print "creating pkg......."
            status , output = commands.getstatusoutput("zip -r  mysite.zip mysite")
            if status == 0:
                return True
            else:
                return False
    else:
        status , output = commands.getstatusoutput("zip -r  mysite.zip mysite")
def  remote_scp():
    t = paramiko.Transport((host,54888))
    t.connect(username=user, password=password)
    sftp = paramiko.SFTPClient.from_transport(t)
    remote_path = "/tmp/mysite.zip"
    local_path = tar_pkg
    print "from localfile %s to remote path %s"%(local_path , remote_path)
    sftp.put(local_path , remote_path)
    print "#######uploaded#######"
    t.close()
    sftp.close()
def remote_cmd():
    command = "scp /tmp/mysite.zip root@dmsag:/tmp/"
    extract = 'ssh dmsag \"unzip -o /tmp/mysite.zip\"'
    sync_to_docker = 'ssh dmsag \"sh /root/mysite/sync2docker.sh\"'
    #extract = 'ssh dmsag \"ls /tmp\"'
    ssh_client = paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh_client.connect(host, 54888 , user, password)
    std_in, std_out, std_err = ssh_client.exec_command(command)
    print "send to dmsag mysite.zip finished"
    print std_out.readlines()
    std_in, std_out, std_err = ssh_client.exec_command(extract)
    print std_out.readlines()
    std_in, std_out, std_err = ssh_client.exec_command(sync_to_docker)
    print std_err.readlines()
    ssh_client.close()
if __name__=='__main__':
    if init():
        print "start sync"
        remote_scp()
        remote_cmd()
    else:
        print "abnormal exit"
    
  
