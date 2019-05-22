from django.urls import path
from . import views

app_name='sql'
urlpatterns=[
    path('',views.index),#主页
    path('query',views.query),#查询
    path('getcheck',views.getCheck),#获取一个验证码
    path('check',views.checkCheck),#验证一个验证码
    path('url',views.checkCheck),#验证一个验证码
]