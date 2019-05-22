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

def surl(requests):#短链接 index
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

def createSUrl(requests):
    if not request.method == 'POST':
        return HttpResponse('失败')
    


def logs(requests):#日志 index
    data={}
    data['toolName']="logs"
    
    return render(requests, 'tools/index.html', data)