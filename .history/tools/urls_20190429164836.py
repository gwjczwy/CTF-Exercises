from django.urls import path
from . import views

app_name='tools'
urlpatterns=[
    path('url/createurl/',views.createSUrl), #短链接
    path('url/',views.surls), #短链接 index
    path('s/<str:parameter>/',views.surl), #带连接参数的短链接
    path('shop/',views.shop),#商店
    path('logs/',views.logs),#商店
    path('',views.index),#主页
]