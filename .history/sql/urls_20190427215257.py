from django.urls import path
from . import views

app_name='artical'
urlpatterns=[
    path('',views.index),#主页
    path('query',views.query),#查询
    path('getcheck',views.getCheck),#获取一个验证码
]