#!/bin/bash
templates="/Users/luvensin/Desktop/github/privateCloudMonitor/mysite/mysite/templates"
funcdir="/Users/luvensin/Desktop/github/privateCloudMonitor/mysite/mysite/basefunc"
site="/Users/luvensin/Desktop/github/privateCloudMonitor/mysite/siteDemo"
config="//Users/luvensin/Desktop/github/privateCloudMonitor/mysite/mysite/config"
setting="/Users/luvensin/Desktop/github/privateCloudMonitor/mysite/mysite/settings.py"
static="/Users/luvensin/Desktop/github/privateCloudMonitor/mysite/mysite/static"
url="/Users/luvensin/Desktop/github/privateCloudMonitor/mysite/mysite/urls.py"
target_templates="/data/mysite/mysite/"
target_funcdir="/data/mysite/mysite/"
target_conf="/data/mysite/mysite/"
target_site="/data/mysite/"
target_setting="/data/mysite/mysite/"
target_url="/data/mysite/mysite/"
ip=`ifconfig bond0|grep inet|awk '{print $2}'|cut -d: -f2`
echo "-------replace database host--------"
sed -Ein 's/[0-9]{1,3}.[0-9]{1,3}.[0-9]{1,3}.[0-9]{1,3}/$ip/g' settings.py
function Ret()
{
    ret=`echo $?`
    if [ $ret -eq 0 ]; then
        echo "complated"
    else
        echo "error"
        exit 255
    fi
}




echo "---------start sync dir into docker-----------"
id=`docker ps |awk '{print $1}'|grep -E "\d+"`
echo $id
echo "---------sync templates------------"
echo $templates
echo $target_templates
docker cp $templates $id:$target_templates
Ret
echo "---------sync funcdir--------------"
docker cp $funcdir $id:$target_funcdir
Ret
echo "---------sync site-----------------"
docker cp $site $id:$target_site
Ret
echo "---------sync static---------------"
docker cp $static $id:$target_funcdir
Ret
echo "---------sync url-------------------"
docker cp $url $id:$target_url
Ret
echo "---------sync setting---------------"
docker cp $setting $id:$target_setting
Ret
echo "---------sync config---------------"
docker cp $config $id:$target_conf
Ret
echo "---------restart docker------------"
docker restart $id
Ret

