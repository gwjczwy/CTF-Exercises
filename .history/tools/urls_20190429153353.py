from django.urls import path
from . import views

app_name='tools'
urlpatterns=[
    path('s/<str:parameter>/',views.surls), #带连接参数的短链接
    path('s/',views.surl), #短链接
    path('shop',views.shop),#商店
    path('logs',views.logs),#商店
    path('',views.index),#主页
]