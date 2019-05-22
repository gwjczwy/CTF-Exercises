from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from json import dumps
import pymysql

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