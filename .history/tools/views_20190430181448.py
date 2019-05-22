from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from json import dumps
from .models import Url,Money
import time

#########################
#主页
@login_required
def index(requests):
    data={'toolname':'index','user':requests.user}
    return render(requests,'tools/index.html',data)

#########################
#短链接
@login_required
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
        return HttpResponse('你来错地方了,悟空')
    req=req.fullUrl
    return HttpResponse('<script>window.location.href="'+req+'";</script>')


@csrf_exempt
@login_required
def createSUrl(requests):
    if not (requests.method == 'POST' and requests.POST['fullUrl']):
        req={'message':'fail'}
        return HttpResponse(dumps(req),content_type="application/json")
    fullUrl=requests.POST['fullUrl']
    while True:
        randUrl=randStr(5)#随机长度为5的字符串
        try:
            Url.objects.get(sUrl=randUrl)#如果重复就继续随机
            print('再!来!一!次!')
        except:
            break
    randUrl=randStr(5)
    Url(sUrl=randUrl,fullUrl=fullUrl).save()
    req={'message':'success','url':randUrl}
    return HttpResponse(dumps(req),content_type="application/json")

def randStr(l):
    import random
    import string
    
    seed = "1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    sa = []
    for i in range(l):
        sa.append(random.choice(seed))
    salt = ''.join(sa)
    return salt


#########################
#商店
@login_required
def shop(requests):
    data={}
    data['toolName']="shop"
    money = Money.objects.get(user=requests.user)
    data['money']=money

    
    return render(requests, 'tools/index.html', data)

#商店兑换
@csrf_exempt
@login_required
def shopExchange(requests):
    if not (requests.method == 'POST' and 'rule' in requests.POST and 'num' in requests.POST):
        print('非法请求')
        req={'message':'fail','reason':'非法请求'}
        return HttpResponse(dumps(req),content_type="application/json")
    rule=requests.POST['rule']
    num=requests.POST['num']
    if not rule in ['m2b','b2m']:# 判断转换规则是否合法
        print('rule参数不合法')
        req={'message':'fail','reason':'rule参数不合法'}
        return HttpResponse(dumps(req),content_type="application/json")
    if num.isdigit():# 判断数字是否合法
        num=int(num)
        if num<0:
            req={'message':'fail','reason':'非法参数'}
            return HttpResponse(dumps(req),content_type="application/json")
    else:
        req={'message':'fail','reason':'非法参数'}
        return HttpResponse(dumps(req),content_type="application/json")
    # 获取货币对象
    money = Money.objects.get(user=requests.user)
    if rule=='m2b':
        if money.monero>=num:
            money.bitcoin+=num
            money.save()
            time.sleep(5)  #等待时间 造成条件竞争
            money.monero-=num
            money.save()
        else:
            req={'message':'fail','reason':'monero 不足'}
            return HttpResponse(dumps(req),content_type="application/json")
    elif rule=='b2m':
        if money.bitcoin>=num:
            money.monero+=num
            money.save()
            time.sleep(5)
            money.bitcoin-=num
            money.save()
        else:
            req={'message':'fail','reason':'bitcoin 不足'}
            return HttpResponse(dumps(req),content_type="application/json")
    else:
        req={'message':'fail','reason':'未知错误'}
        return HttpResponse(dumps(req),content_type="application/json")


    req={'message':'success','monero':money.monero,'bitcoin':money.bitcoin}
    return HttpResponse(dumps(req),content_type="application/json")



#########################
#日志
@login_required
def logs(requests):
    data={}
    data['toolName']="logs"
    
    return render(requests, 'tools/index.html', data)

# 添加日志
@csrf_exempt
@login_required
def addLog(requests):
