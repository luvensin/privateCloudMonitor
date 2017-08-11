"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from mysite.views import HELLO,home_page,template_demo,template_demo2,template_demo3,template_demo4
#from siteDemo.tests import current_url,user_agent,display_meta,search_Auth,search,bootstrap_demo,home
from siteDemo.views import OssDataShow , offline_ecs_pangu,shutdown_ecs_pangu,ecsDataPangu, homePage, ecsPage ,ecsData , lock , unlock , dataAnalysis , mainPage , parseConf , getConf , EcsDataShow , ecsDataPanel

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$' , homePage),

    url(r'^ecs$' , ecsPage),
    url(r'data/ecsdata/', ecsData , name="ecsData" ),
    url(r'ecs/nc_lock/' , lock , name='lock'),
    url(r'ecs/nc_unlock/' , unlock , name='unlock'),

    url(r'^resourceAnalysis/$', dataAnalysis),
    url(r'mainPage/' , mainPage , name="mainPage"),

    url(r'EcsDataShow/' , EcsDataShow , name="EcsDataShow"),
    url(r'EcsDataPanel/' , ecsDataPanel , name='EcsDataPanel'),
    url(r'EcsDataPangu/' , ecsDataPangu , name='EcsDataPangu'),
    url(r'offline_ecs_pangu/', offline_ecs_pangu , name="offline_ecs_pangu"),
    url(r'shutdown_ecs_pangu/', shutdown_ecs_pangu , name='shutdown_ecs_pangu'),

    url(r'OssDataShow/' , OssDataShow , name="OssDataShow"),



    url(r'config$' , parseConf ),
    url(r'confPost/' ,getConf , name="confPost" )

]
