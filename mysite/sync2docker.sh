#!/bin/bash
templates="/root/mysite/mysite/templates"
funcdir="/root/mysite/mysite/basefunc"
site="/root/mysite/siteDemo"
config="/root/mysite/mysite/config"
setting="/root/mysite/mysite/settings.py"
static="/root/mysite/mysite/static"
url="/root/mysite/mysite/urls.py"
target_templates="/data/mysite/mysite/"
target_funcdir="/data/mysite/mysite/"
target_conf="/data/mysite/mysite/"
target_site="/data/mysite/"
target_setting="/data/mysite/mysite/"
target_url="/data/mysite/mysite/"
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
id=`docker ps |grep delivery|awk '{print $1}'`
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

