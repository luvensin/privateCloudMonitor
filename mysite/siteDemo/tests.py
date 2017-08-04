# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
from django.http import HttpResponse
from django.shortcuts import render_to_response
from models import Author
def current_url(request):
	path = request.path
	hosts = request.get_host()
	fullPath = request.get_full_path()
	isHttps = request.is_secure()

	return HttpResponse("%s , %s , %s , %s"%(path,hosts,fullPath,isHttps))
# Create your tests here.

def user_agent(request):
	ua = request.META['HTTP_USER_AGENT']
	al = request.META
	return HttpResponse('user_agent = %s'%ua)

def display_meta(request):
    values = request.META.items()
    values.sort()
    html = []
    for k, v in values:
        html.append('<tr><td>%s</td><td>%s</td></tr>' % (k, v))
    print html
    return HttpResponse('<table>%s</table>' % '\n'.join(html))

def search_Auth(request):
	return render_to_response('search.html')

def search(request):
	if 'q' in request.GET and request.GET['q']:
		try:
			email = Author.objects.filter(name=request.GET['q']).values()[0]['email']
		except Exception as e:
			email = "没找到"
		data = '他/她 的email是%s '%(email)
		return render_to_response('search.html',{'result' : data})
	else:
		return render_to_response("search.html",{'error' : True})
def bootstrap_demo(request):
	return render_to_response('bootstrap-alerts-on-error-success-and-information.html') 

def home(request):
	return render_to_response("root.html")