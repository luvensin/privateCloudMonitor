#-*- coding:utf-8 -*-
from django.http import HttpResponse
import sys
import datetime
from django.template import Template, Context
from django.template.loader import get_template
from django.shortcuts import render_to_response
from datetime import datetime,timedelta
reload(sys)
sys.setdefaultencoding('utf-8')


def HELLO(request):
    return HttpResponse("my first mvc")
def home_page(request,offset):
    now = datetime.datetime.now()
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()
    html = "<html><body>It is now %s,%s.</body></html>" % (now,offset)
    return HttpResponse(html)
def template_demo(request):
    tmp = '/Users/luvensin/Desktop/Scripts/mysite/mysite/templates/test.html'
    data = open(tmp,'rb')
    html = data.read()
    t = Template(html)
    c = Context({'person_name': 'luvensin',
              'company': 'dtdream',
              'ship_date': datetime.date(2009, 4, 2),
              'ordered_warranty': True})
    data.close()
    html_ = t.render(c)
    return HttpResponse(html_)
def template_demo2(request):
    update = {}
    #t = get_template('test.html')
    update = {'person_name': 'luvensin',
              'company': 'dtdream',
              'ship_date': datetime.now(),
              'ordered_warranty': True}
    #html = t.render(Context(update))
    #return HttpResponse(html)
    '''使用rander_to_response 可节省大量时间，直接封装好的，可以直接调用html 并传入参数而且直接会渲染'''
    return render_to_response('test.html',update)
def template_demo3(request):
    update = {'current_date':datetime.now()}
    return render_to_response('current_time.html',update)
def template_demo4(request,offset):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()
    dt = datetime.now() + timedelta(hours=offset)
    update = {'hour_offset':offset,"next_time":dt}
    return render_to_response('hours.html',update)

#if __name__ == '__main__':
#    template_demo()
