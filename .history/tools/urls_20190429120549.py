from django.urls import path
from . import views

app_name='tools'
urlpatterns=[
    path('s',views.surl),#短链接
    path('shop',views.shop),#商店
    path('',views.index),#主页
]