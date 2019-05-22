from django.urls import path
from . import views

app_name='tools'
urlpatterns=[
    path('url/createurl/',views.createSUrl), #创建短链接
    path('url/',views.surl), #短链接 index
    path('s/<str:parameter>/',views.surls), #带跳转参数的短链接
    path('s/',views.surl), #短链接 index
    path('shop/',views.shop),#商店
    path('shop/shopExchange',views.shopExchange),#商店兑换
    path('logs/',views.logs),#日志
    path('logs/add',views.addLog),#添加日志
    path('logs/getLog',views.getLog),#获取日志
    path('logs/downSource',views.downSource),#下载网站源码
    path('index/',views.index),#主页
]
urlpatterns.append(path('haha/',views.index))
