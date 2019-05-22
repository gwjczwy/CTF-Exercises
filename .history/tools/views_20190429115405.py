from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse


def index(requests):
    return render(requests,'tools/index.html')

def shop(requests):
    data={}
    data['toolName']="shop"
    return render(requests, 'tools/index.html', data)