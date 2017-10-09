# privateCloudMonitor

1， 主界面
主界面主要是平台内部管控所需的一些数据库链接字符串、url，将常用的维护信息集中到一块，方便运维人员粘贴复制&登陆

![image](https://github.com/luvensin/privateCloudMonitor/blob/master/mainpage.png)

2，产品界面
定义了各个产品所用的物理机的信息已经物理机是否down机，和角色，还有上线下线、锁定解锁等操作
![image](https://github.com/luvensin/privateCloudMonitor/blob/master/productPage.png)

3，产品分析页面，可以看各种资源的占比，即使对整个集群或者单台机器进行资源监控
![image](https://github.com/luvensin/privateCloudMonitor/blob/master/product%20analysis.png)

4，配置页面
如果有新的管控数据库或者是新的url页面加入，可以添加在此处，会展示在1中
![image](https://github.com/luvensin/privateCloudMonitor/blob/master/configPage.png)


系统功能还在完善中，不过ui有点难看，正在开发另一个版本，功能完善的同时增加更合理的人机界面。

发布是通过docker来发布的docker使用ngix镜像docker，将整个项目发布到内，然后打成tar包这样发布就方便多了
Django nginx 发布


docker run -d -i -t -p 8099:8099 e3aac827c00e /bin/bash

docker run -d -p 8099:8099 --net=host --restart=always --name dt_delivery_v1.0 0e3417977319  -v /bin/bash

注意：内外端口要一致
