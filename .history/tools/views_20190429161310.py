from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from .models import Url


def index(requests):
    return render(requests,'tools/index.html',{'toolname':'index'})

def shop(requests):
    data={}
    data['toolName']="shop"
    return render(requests, 'tools/index.html', data)

def surl(requests):#直接访问短链接创建页面
    data={}
    data['toolName']="surl"
    data['parameter']="index"
    return render(requests, 'tools/index.html', data)

def surls(requests,parameter):#带参数的短链接跳转
    data={}
    data['toolName']="surl"
    data['parameter']="link"
    print('短链接参数',parameter)

    try:
        req=Url.objects.get(sUrl=parameter)
        print('获取对象成功')
    except:
        return ''
    req=req.fullUrl
    return HttpResponse('<script>window.location.href="'+req+'";</script>')

def logs(requests):
    data={}
    data['toolName']="logs"
    
    return render(requests, 'tools/index.html', data)