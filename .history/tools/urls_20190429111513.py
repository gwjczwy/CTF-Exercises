from django.urls import path
from . import views

app_name='artical'
urlpatterns=[
    path('',views.index),#主页
]