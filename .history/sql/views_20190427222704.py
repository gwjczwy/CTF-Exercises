from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from json import dumps
import pymysql
from sql.models import Check
from time import time
from random import randint

# Create your views here.

def index(requests):
    return render(requests,'sql/index.html')

def add2file(path,content):
    with open(path,'at') as f:
        f.write(content+'\n')

@csrf_exempt
def query(requests):
    if requests.method=='POST':
        keyWord=requests.POST['content']
        add2file('./cont.txt',keyWord)
        keyWord.lower()
        for i in ['union']:
            if i in keyWord:
                req={'message':'fall','content':'非法关键字'}
                return HttpResponse(dumps(req),content_type="application/json")
        print(keyWord)
        if 1==1:
            #进行查询
            # 打开数据库连接
            db = pymysql.connect("127.0.0.1","root","root","django" )
            
            # 使用 cursor() 方法创建一个游标对象 cursor
            cursor = db.cursor()
            
            # 使用 execute()  方法执行 SQL 查询 
            cursor.execute("select name,url from github where `name` like '%"+keyWord+"%'")
            
            content=[]
            # 使用 fetchone() 方法获取单条数据.
            for data in cursor.fetchall():
                content.append('<a href="'+data[1]+'" class="list-group-item">'+data[0]+'</a>')
        try:
            #返回结果
            req={'message':'success','content':content}
            return HttpResponse(dumps(req),content_type="application/json")
        except Exception: #捕获所有异常
            #如果发生异常，则回滚
            print("发生异常",Exception)
            db.rollback()
            db.close()
        
    elif requests.method=='GET':
        return HttpResponse("亲这是GET请求了哦,要使用POST请求")
    else:
        return HttpResponse("亲这是$*#%请求了哦,要使用POST请求")

def getCheck(requests):
    id=str(randint(1,10000000))
    a=randint(1,100)
    b=randint(1,100)
    value=str(a*b)
    date=int(time())
    c=Check(checkId=id,checkValue=value,checkDate=date)
    c.save()
    req={'message':'success','content':(id,value,date)}
    return HttpResponse(dumps(req),content_type="application/json")

@csrf_exempt
def checkCheck(requests):
    if requests.method=='POST':
        try:
            id=requests.POST['checkId']
            value=requests.POST['checkValue']
        except:
            req={'message':'fall','content':"验证码错误"}
            return HttpResponse(dumps(req),content_type="application/json")
        try:
            c=Check.objects.get(checkId=id)
            print('获取check对象成功..')
        except:
            print('id号不存在..')
            req={'message':'fall','content':"验证码错误"}
            return HttpResponse(dumps(req),content_type="application/json")
        if int(time())-c.checkDate<=70000:
            if c.checkValue==value:
                print('验证码正确..')
                c.checkDate=1000000   #验证码正确就设置时间为很早以前
                c.save()
                req={'message':'true','content':"验证码正确"}
                return HttpResponse(dumps(req),content_type="application/json")
            else:
                print('验证码对不上号..')
                req={'message':'fall','content':"验证码错误"}
                return HttpResponse(dumps(req),content_type="application/json")
        else:
            print('超时了...')
            req={'message':'fall','content':"验证码错误"}
            return HttpResponse(dumps(req),content_type="application/json")
    else:
        req={'message':'fall','content':"验证码错误"}
        return HttpResponse(dumps(req),content_type="application/json")