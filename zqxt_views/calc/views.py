# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def add(Request):
    a = Request.GET['a']
    b = Request.GET['b']
    c = int(a) + int(b)
    return HttpResponse(str(c))
    #URL format is:http://127.0.0.1:8000/add/?a=111&b=333

def add2(Request,a,b):
    c = int(a) + int(b)
    return HttpResponse(str(c))
    #URL format is:http://127.0.0.1:8000/add/111/333

def subtract(Request,a,b):
    w = int(a) - int(b)
    return HttpResponse((w))
    #URL format is:http://127.0.0.1:8000/subtract/111/333

def multiply(Request,a,b):
    h = int(a) * int(b)
    return HttpResponse(str(h))
    #URL format is:http://127.0.0.1:8000/multiply/111/333

def divide(request,a,b):
    if float(b) == 0:
        return HttpResponse(u'0不能作为除数')
    else:
        k = int(a) / int(b)
    return HttpResponse(str(k))
    #URL format is:http://127.0.0.1:8000/divide/111/333



