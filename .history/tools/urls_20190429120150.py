from django.urls import path
from . import views

app_name='tools'
urlpatterns=[
    path('shop',views.shop),#主页
    path('',views.index),#主页
]