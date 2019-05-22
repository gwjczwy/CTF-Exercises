from django.urls import path
from . import views

app_name='tools'
urlpatterns=[
    path('',views.index),#主页
]